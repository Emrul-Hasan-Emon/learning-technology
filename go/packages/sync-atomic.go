package main

/*
SYNC/ATOMIC PACKAGE - LOCK-FREE SYNCHRONIZATION
================================================

The atomic package provides low-level atomic memory primitives for implementing
synchronization algorithms without locks. Operations are performed atomically,
meaning they complete without interruption.

WHY USE ATOMIC:
===============
1. LOCK-FREE PERFORMANCE: No locks = no waiting, better throughput
2. SIMPLE OPERATIONS: Perfect for counters, flags, and simple value updates
3. REDUCED CONTENTION: Multiple goroutines can proceed concurrently
4. LOWER LATENCY: No lock acquisition/release overhead
5. PREVENTS RACE CONDITIONS: Hardware-level atomic operations

SUPPORTED TYPES:
================
- int32, int64
- uint32, uint64
- uintptr
- unsafe.Pointer
- Bool, Int32, Int64, Uint32, Uint64, Uintptr, Pointer (generic types in Go 1.19+)

KEY OPERATIONS:
===============
- Add(): Atomically add a value
- Load(): Atomically read a value
- Store(): Atomically write a value
- Swap(): Atomically swap values
- CompareAndSwap(): Conditional atomic write

WHEN TO USE ATOMIC vs MUTEX:
=============================
USE ATOMIC when:
  - Operating on single primitive values (counters, flags)
  - Read-heavy or write-heavy workloads with simple operations
  - Performance is critical and contention is expected

USE MUTEX when:
  - Protecting complex data structures
  - Multiple operations must be atomic as a group
  - Simplicity is more important than raw performance

BEST PRACTICES:
===============
- Use for simple types only (counters, flags, pointers)
- Copy atomic values by value, not by pointer
- Never embed atomic types in structs passed by value
*/

import (
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

/*
EXAMPLE 1: Atomic Counter - Load & Store
========================================
Basic atomic operations for reading and writing counter values.
*/
func example1AtomicCounter() {
	fmt.Println("\n=== EXAMPLE 1: Atomic Counter (Load & Store) ===")

	var counter atomic.Int64

	// Increment atomically
	for i := 0; i < 100; i++ {
		go func() {
			counter.Add(1)
		}()
	}

	time.Sleep(50 * time.Millisecond)

	// Read atomically
	value := counter.Load()
	fmt.Printf("Final counter value: %d\n", value)
}

/*
EXAMPLE 2: Atomic Add - Efficient Counting
=========================================
Add() is more efficient than Load-modify-Store for incrementing.
*/
func example2AtomicAdd() {
	fmt.Println("\n=== EXAMPLE 2: Atomic Add (Efficient Counting) ===")

	var requestCount atomic.Int64

	for i := 0; i < 10; i++ {
		go func() {
			for j := 0; j < 50; j++ {
				requestCount.Add(1)
				time.Sleep(time.Microsecond) // Simulate request handling
			}
		}()
	}

	time.Sleep(600 * time.Millisecond)
	fmt.Printf("Total requests processed: %d\n", requestCount.Load())
}

/*
EXAMPLE 3: Atomic Swap - Update and Get Old Value
================================================
Swap() atomically updates value and returns the previous value.
*/
func example3AtomicSwap() {
	fmt.Println("\n=== EXAMPLE 3: Atomic Swap ===")

	var status atomic.Int32
	status.Store(0) // 0 = idle

	for i := 0; i < 5; i++ {
		go func(id int) {
			// Swap from 0 (idle) to 1 (busy)
			oldStatus := status.Swap(1)
			if oldStatus == 0 {
				fmt.Printf("Goroutine %d: transitioned from idle to busy\n", id)
				time.Sleep(50 * time.Millisecond)
				status.Store(0) // Back to idle
				fmt.Printf("Goroutine %d: back to idle\n", id)
			}
		}(i)
	}

	time.Sleep(300 * time.Millisecond)
}

/*
EXAMPLE 4: CompareAndSwap - Conditional Update
==============================================
CAS (Compare-And-Swap) atomically updates only if current value matches expected.
Foundation for lock-free algorithms.
*/
func example4CompareAndSwap() {
	fmt.Println("\n=== EXAMPLE 4: CompareAndSwap (CAS) ===")

	var version atomic.Int32
	version.Store(1)

	for i := 0; i < 10; i++ {
		go func(id int) {
			for attempts := 0; attempts < 3; attempts++ {
				current := version.Load()
				next := current + 1

				// Try to update from current to next
				if version.CompareAndSwap(current, next) {
					fmt.Printf("Goroutine %d: updated version %d -> %d\n", id, current, next)
					return
				}
				fmt.Printf("Goroutine %d: CAS failed (conflict), retrying\n", id)
			}
		}(i)
	}

	time.Sleep(100 * time.Millisecond)
	fmt.Printf("Final version: %d\n", version.Load())
}

/*
EXAMPLE 5: Atomic Bool - Thread-Safe Flags
=========================================
Using atomic Bool for flags that control goroutines.
*/
func example5AtomicBool() {
	fmt.Println("\n=== EXAMPLE 5: Atomic Bool (Flags) ===")

	var running atomic.Bool
	running.Store(true)

	// Worker goroutines check flag
	for i := 0; i < 3; i++ {
		go func(id int) {
			for running.Load() {
				fmt.Printf("Worker %d: running\n", id)
				time.Sleep(50 * time.Millisecond)
			}
			fmt.Printf("Worker %d: stopped\n", id)
		}(i)
	}

	time.Sleep(150 * time.Millisecond)
	running.Store(false) // Stop all workers

	time.Sleep(100 * time.Millisecond)
	fmt.Println("All workers stopped")
}

/*
EXAMPLE 6: Atomic Pointer - Lock-Free Pointer Updates
====================================================
Using atomic for pointer updates (useful for config reloading, etc).
*/
func example6AtomicPointer() {
	fmt.Println("\n=== EXAMPLE 6: Atomic Pointer ===")

	type Config struct {
		timeout int
		retries int
	}

	var config atomic.Pointer[Config]
	config.Store(&Config{timeout: 30, retries: 3})

	// Reader goroutines
	for i := 0; i < 5; i++ {
		go func(id int) {
			cfg := config.Load()
			fmt.Printf("Reader %d: timeout=%d, retries=%d\n", id, cfg.timeout, cfg.retries)
		}(i)
	}

	time.Sleep(50 * time.Millisecond)

	// Update config
	newConfig := &Config{timeout: 60, retries: 5}
	oldConfig := config.Swap(newConfig)
	fmt.Printf("Config updated from: timeout=%d to %d\n", oldConfig.timeout, newConfig.timeout)
}

/*
EXAMPLE 7: Atomic vs Mutex - Performance Difference
==================================================
Demonstrates why atomic is faster for simple operations.
*/
func example7PerformanceComparison() {
	fmt.Println("\n=== EXAMPLE 7: Atomic vs Mutex - Performance ===")

	// Using atomic (fast)
	var atomicCounter atomic.Int64
	start := time.Now()
	for i := 0; i < 1000000; i++ {
		atomicCounter.Add(1)
	}
	atomicTime := time.Since(start)

	// Using mutex (slower)
	var counterMutex int64
	var mu sync.Mutex
	start = time.Now()
	for i := 0; i < 1000000; i++ {
		mu.Lock()
		counterMutex++
		mu.Unlock()
	}
	mutexTime := time.Since(start)

	fmt.Printf("Atomic time: %v microseconds\n", atomicTime.Microseconds())
	fmt.Printf("Mutex time:  %v microseconds\n", mutexTime.Microseconds())
	fmt.Printf("Atomic is ~%.1fx faster\n", float64(mutexTime)/float64(atomicTime))
}

/*
EXAMPLE 8: Load-Link Store-Conditional Pattern
==============================================
Simulating retry loop for complex operations using CAS.
*/
func example8RetryPattern() {
	fmt.Println("\n=== EXAMPLE 8: CAS Retry Pattern ===")

	var failureCount atomic.Int32

	for i := 0; i < 5; i++ {
		go func(id int) {
			for retries := 0; retries < 3; retries++ {
				current := failureCount.Load()

				// Simulate some work before CAS
				time.Sleep(time.Microsecond)

				// Try to atomically update
				if failureCount.CompareAndSwap(current, current+1) {
					if retries > 0 {
						fmt.Printf("Goroutine %d: succeeded after %d retries\n", id, retries)
					}
					return
				}
				fmt.Printf("Goroutine %d: CAS failed, retry %d\n", id, retries+1)
			}
		}(i)
	}

	time.Sleep(50 * time.Millisecond)
	fmt.Printf("Total failures (CAS operations): %d\n", failureCount.Load())
}

/*
EXAMPLE 9: Atomic Counter in Metrics Collection
===============================================
Real-world example: collecting metrics from multiple goroutines.
*/
func example9MetricsCollection() {
	fmt.Println("\n=== EXAMPLE 9: Metrics Collection ===")

	type Metrics struct {
		requests  atomic.Int64
		errors    atomic.Int64
		latency   atomic.Int64
	}

	metrics := &Metrics{}

	// Simulate request handlers
	for i := 0; i < 10; i++ {
		go func(id int) {
			for j := 0; j < 10; j++ {
				metrics.requests.Add(1)

				// Simulate random error (1 in 5 chance)
				if j%5 == 0 {
					metrics.errors.Add(1)
					fmt.Printf("Handler %d: error\n", id)
				}

				time.Sleep(10 * time.Millisecond)
			}
		}(i)
	}

	time.Sleep(200 * time.Millisecond)

	fmt.Printf("Total requests: %d\n", metrics.requests.Load())
	fmt.Printf("Total errors: %d\n", metrics.errors.Load())
	fmt.Printf("Success rate: %.1f%%\n", 
		float64(metrics.requests.Load()-metrics.errors.Load())/float64(metrics.requests.Load())*100)
}

/*
EXAMPLE 10: Spinlock - CAS-Based Lock
====================================
Demonstrating how to build a simple spinlock using CAS.
*/
func example10Spinlock() {
	fmt.Println("\n=== EXAMPLE 10: Spinlock Using CAS ===")

	type Spinlock struct {
		locked atomic.Bool
	}

	lock := &Spinlock{}

	criticalSection := func(id int) {
		// Spin until we acquire lock
		for !lock.locked.CompareAndSwap(false, true) {
			// Spin (in real code, might use time.Sleep to be polite)
			time.Sleep(time.Microsecond)
		}

		fmt.Printf("Goroutine %d: entered critical section\n", id)
		time.Sleep(50 * time.Millisecond)
		fmt.Printf("Goroutine %d: leaving critical section\n", id)

		lock.locked.Store(false) // Release lock
	}

	for i := 0; i < 3; i++ {
		go criticalSection(i)
	}

	time.Sleep(300 * time.Millisecond)
	fmt.Println("All goroutines completed")
}

func main() {
	example1AtomicCounter()
	example2AtomicAdd()
	example3AtomicSwap()
	example4CompareAndSwap()
	example5AtomicBool()
	example6AtomicPointer()
	example7PerformanceComparison()
	example8RetryPattern()
	example9MetricsCollection()
	example10Spinlock()
}
