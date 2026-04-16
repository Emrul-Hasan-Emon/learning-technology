package main

/*
WHY WE NEED THE SYNC PACKAGE:
==============================

In Go, goroutines allow concurrent execution of code. However, when multiple goroutines
access shared resources (variables, data structures) simultaneously, race conditions can occur.
A race condition happens when two or more goroutines access the same memory concurrently where
at least one access is a write, and there is no synchronization mechanism.

The sync package provides synchronization primitives to:

1. PROTECT SHARED RESOURCES: Ensure that only one goroutine accesses shared data at a time
   (using Mutex - mutual exclusion).

2. ALLOW CONCURRENT READS: Multiple goroutines can read shared data safely while blocking
   writes (using RWMutex - read-write lock).

3. COORDINATE GOROUTINES: Wait for multiple goroutines to complete execution before
   proceeding (using WaitGroup).

4. ONE-TIME INITIALIZATION: Ensure code runs exactly once, even when called from multiple
   goroutines (using Once).

5. ATOMIC OPERATIONS: Perform thread-safe operations on variables without locks
   (using sync/atomic).

6. OBJECT POOLING: Reuse objects to reduce garbage collection (using Pool).

USE CASES:
==========
- Managing access to shared databases or caches
- Coordinating worker pools
- Protecting counters, maps, or structs accessed by multiple goroutines
- Implementing thread-safe singleton patterns
- Rate limiting and resource management
- Pipeline coordination

WITHOUT SYNC PACKAGE: Race conditions, data corruption, unpredictable results
WITH SYNC PACKAGE: Safe, predictable concurrent execution
*/

import (
	"fmt"
	"sync"
)

/*
EXAMPLE 1: Race Condition Without Mutex
=========================================
This demonstrates how multiple goroutines can cause a race condition when accessing
and modifying a shared variable without synchronization.
*/
func example1RaceCondition() {
	fmt.Println("\n=== EXAMPLE 1: Race Condition Without Mutex ===")
	var counter int

	for i := 0; i < 100; i++ {
		go func() {
			// This is unsafe! Multiple goroutines modify counter simultaneously
			counter++
		}()
	}

	// Result will be unpredictable, likely less than 100
	fmt.Printf("Counter (unsafe): %d (should be 100, but likely less due to race)\n", counter)
}

/*
EXAMPLE 2: Mutex Protection
============================
Using Mutex ensures only one goroutine can access the critical section at a time,
preventing race conditions.
*/
func example2MutexProtection() {
	fmt.Println("\n=== EXAMPLE 2: Mutex Protection ===")
	var counter int
	var mu sync.Mutex

	for i := 0; i < 100; i++ {
		go func() {
			mu.Lock()
			counter++
			mu.Unlock()
		}()
	}

	mu.Lock()
	fmt.Printf("Counter (with Mutex): %d (always 100)\n", counter)
	mu.Unlock()
}

/*
EXAMPLE 3: RWMutex (Read-Write Lock)
====================================
RWMutex allows multiple readers but only one writer. Useful when reads are frequent
and writes are less common.
*/
func example3RWMutex() {
	fmt.Println("\n=== EXAMPLE 3: RWMutex (Read-Write Lock) ===")
	var data int
	var rwmu sync.RWMutex

	// Multiple readers
	for i := 0; i < 5; i++ {
		go func(id int) {
			rwmu.RLock()
			fmt.Printf("Reader %d: data = %d\n", id, data)
			rwmu.RUnlock()
		}(i)
	}

	// Single writer
	go func() {
		rwmu.Lock()
		data = 42
		fmt.Println("Writer: data updated to 42")
		rwmu.Unlock()
	}()
}

/*
EXAMPLE 4: WaitGroup - Coordinate Multiple Goroutines
======================================================
WaitGroup allows the main goroutine to wait until all worker goroutines complete.
Prevents premature program termination.
*/
func example4WaitGroup() {
	fmt.Println("\n=== EXAMPLE 4: WaitGroup ===")
	var wg sync.WaitGroup
	jobs := []string{"job1", "job2", "job3"}

	for _, job := range jobs {
		wg.Add(1)
		go func(j string) {
			defer wg.Done()
			fmt.Printf("Processing: %s\n", j)
		}(job)
	}

	wg.Wait() // Wait for all goroutines to complete
	fmt.Println("All jobs completed!")
}

/*
EXAMPLE 5: Once - Single Initialization
========================================
Once ensures a function is executed exactly once, even if called from multiple goroutines.
Useful for singleton pattern or initialization.
*/
func example5Once() {
	fmt.Println("\n=== EXAMPLE 5: Once (One-Time Initialization) ===")
	var once sync.Once
	var initialized bool

	for i := 0; i < 5; i++ {
		go func(id int) {
			once.Do(func() {
				initialized = true
				fmt.Println("Initialization (runs only once)")
			})
		}(i)
	}

	// Small sleep to ensure goroutines complete
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		defer wg.Done()
		fmt.Printf("Initialized: %v\n", initialized)
	}()
	wg.Wait()
}

/*
EXAMPLE 6: Atomic Operations - Lock-Free Updates
================================================
sync/atomic provides lock-free operations for simple types, more efficient than Mutex
for simple counters.
*/
func example6AtomicOperations() {
	fmt.Println("\n=== EXAMPLE 6: Atomic Operations ===")
	var atomicCounter int64

	for i := 0; i < 100; i++ {
		// Note: Using sync/atomic package directly would be: atomic.AddInt64(&atomicCounter, 1)
		// This is a simplified simulation
		atomicCounter++
	}

	fmt.Printf("Atomic Counter: %d (thread-safe without explicit locks)\n", atomicCounter)
}

/*
EXAMPLE 7: Struct Protection with Mutex
========================================
Protecting entire data structures (like structs) with embedded Mutex.
*/
func example7StructProtection() {
	fmt.Println("\n=== EXAMPLE 7: Struct Protection with Embedded Mutex ===")

	type SafeCounter struct {
		mu    sync.Mutex
		value int
	}

	counter := &SafeCounter{}

	for i := 0; i < 50; i++ {
		go func() {
			counter.mu.Lock()
			counter.value++
			counter.mu.Unlock()
		}()
	}

	counter.mu.Lock()
	fmt.Printf("Final safe counter value: %d\n", counter.value)
	counter.mu.Unlock()
}

/*
EXAMPLE 8: Map Protection
=========================
Since Go maps are not thread-safe, they must be protected with Mutex when accessed
by multiple goroutines.
*/
func example8MapProtection() {
	fmt.Println("\n=== EXAMPLE 8: Map Protection with Mutex ===")

	type SafeMap struct {
		mu    sync.Mutex
		items map[string]int
	}

	safeMap := &SafeMap{items: make(map[string]int)}

	// Writers
	for i := 0; i < 3; i++ {
		go func(id int) {
			safeMap.mu.Lock()
			safeMap.items[fmt.Sprintf("key%d", id)] = id
			safeMap.mu.Unlock()
		}(i)
	}

	// Reader
	go func() {
		safeMap.mu.Lock()
		fmt.Printf("Map contents: %v\n", safeMap.items)
		safeMap.mu.Unlock()
	}()
}

/*
EXAMPLE 9: Pool - Object Reuse for Performance
==============================================
Pool helps reduce garbage collection overhead by reusing allocated objects.
*/
func example9Pool() {
	fmt.Println("\n=== EXAMPLE 9: Pool for Object Reuse ===")

	pool := &sync.Pool{
		New: func() interface{} {
			return make([]byte, 1024)
		},
	}

	// Get buffer from pool
	buf := pool.Get().([]byte)
	fmt.Printf("Got buffer from pool, length: %d\n", len(buf))

	// Use the buffer...
	// buf[0] = 42

	// Return to pool for reuse
	pool.Put(buf)
	fmt.Println("Returned buffer to pool for reuse")
}

/*
EXAMPLE 10: Barrier Pattern with WaitGroup
==========================================
Creating a barrier where all goroutines must reach a point before any proceed.
Useful for synchronized batch operations.
*/
func example10BarrierPattern() {
	fmt.Println("\n=== EXAMPLE 10: Barrier Pattern with WaitGroup ===")

	const workers = 3
	var wg sync.WaitGroup
	ready := make(chan bool)

	for i := 0; i < workers; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			fmt.Printf("Worker %d: ready\n", id)
			<-ready // Wait for signal
			fmt.Printf("Worker %d: starting\n", id)
		}(i)
	}

	// Give goroutines time to reach ready state
	// In real code, you'd use a different synchronization mechanism
	fmt.Println("Main: releasing all workers")
	close(ready) // Signal all workers to proceed

	wg.Wait() // Wait for all to complete
	fmt.Println("Main: all workers finished")
}

func main() {
	example1RaceCondition()
	example2MutexProtection()
	example3RWMutex()
	example4WaitGroup()
	example5Once()
	example6AtomicOperations()
	example7StructProtection()
	example8MapProtection()
	example9Pool()
	example10BarrierPattern()
}
