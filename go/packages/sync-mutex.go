package main

/*
SYNC PACKAGE - MUTEX (MUTUAL EXCLUSION)
========================================

A Mutex is a synchronization primitive that protects shared resources from concurrent access.
Only one goroutine can hold the lock at a time, making others wait until the lock is released.

WHY USE MUTEX:
==============
1. PREVENT RACE CONDITIONS: Ensures only one goroutine accesses critical sections
2. DATA CONSISTENCY: Protects data structures from corruption
3. SAFE MAP/SLICE ACCESS: Go maps and slices are not thread-safe
4. PROTECT COUNTERS: Ensures accurate counting in concurrent scenarios
5. SERIALIZED ACCESS: When operations must execute in isolation

KEY METHODS:
============
- Lock(): Acquires the lock (blocks if locked by another goroutine)
- Unlock(): Releases the lock (panics if not locked)
- TryLock(): Attempts to acquire lock without blocking (Go 1.18+, returns bool)

BEST PRACTICES:
===============
- Always pair Lock() with Unlock() (use defer to guarantee unlock)
- Keep critical sections small (minimize time lock is held)
- Avoid nested locks (can cause deadlocks)
- Use RWMutex for read-heavy workloads
*/

import (
	"fmt"
	"sync"
	"time"
)

/*
EXAMPLE 1: Basic Mutex - Protecting a Counter
==============================================
Demonstrates how Mutex prevents race conditions when incrementing a shared counter.
*/
func example1BasicMutex() {
	fmt.Println("\n=== EXAMPLE 1: Basic Mutex - Counter Protection ===")

	type Counter struct {
		mu    sync.Mutex
		value int
	}

	counter := &Counter{}

	// Increment counter 1000 times from 10 goroutines
	for i := 0; i < 10; i++ {
		go func() {
			for j := 0; j < 100; j++ {
				counter.mu.Lock()
				counter.value++
				counter.mu.Unlock()
			}
		}()
	}

	time.Sleep(100 * time.Millisecond) // Wait for goroutines
	counter.mu.Lock()
	fmt.Printf("Final counter value: %d (always 1000, never less)\n", counter.value)
	counter.mu.Unlock()
}

/*
EXAMPLE 2: Mutex with Defer - Guaranteed Unlock
================================================
Using defer ensures Unlock is called even if code panics, preventing deadlocks.
*/
func example2MutexWithDefer() {
	fmt.Println("\n=== EXAMPLE 2: Mutex with Defer ===")

	type SafeValue struct {
		mu    sync.Mutex
		value int
	}

	safe := &SafeValue{}

	// Good practice: use defer to guarantee unlock
	for i := 0; i < 3; i++ {
		go func(id int) {
			safe.mu.Lock()
			defer safe.mu.Unlock() // Guaranteed to run

			safe.value = id
			fmt.Printf("Goroutine %d: set value to %d\n", id, safe.value)

			// Even if something panics here, Unlock will still run
		}(i)
	}

	time.Sleep(50 * time.Millisecond)
	safe.mu.Lock()
	fmt.Printf("Final value: %d\n", safe.value)
	safe.mu.Unlock()
}

/*
EXAMPLE 3: Protected Map - Thread-Safe Access
==============================================
Maps in Go are not thread-safe. Mutex must protect all access.
*/
func example3ProtectedMap() {
	fmt.Println("\n=== EXAMPLE 3: Protected Map ===")

	type SafeMap struct {
		mu    sync.Mutex
		items map[string]int
	}

	safeMap := &SafeMap{items: make(map[string]int)}

	// Writers
	for i := 0; i < 5; i++ {
		go func(id int) {
			key := fmt.Sprintf("key%d", id)
			safeMap.mu.Lock()
			safeMap.items[key] = id * 10
			safeMap.mu.Unlock()
			fmt.Printf("Writer %d: inserted %s -> %d\n", id, key, id*10)
		}(i)
	}

	// Readers
	for i := 0; i < 3; i++ {
		go func(readerID int) {
			time.Sleep(10 * time.Millisecond) // Let writers finish
			safeMap.mu.Lock()
			fmt.Printf("Reader %d: map size = %d\n", readerID, len(safeMap.items))
			safeMap.mu.Unlock()
		}(i)
	}

	time.Sleep(100 * time.Millisecond)
}

/*
EXAMPLE 4: Protected Struct - Encapsulated Locking
==================================================
Best practice: embed Mutex in the struct that needs protection.
*/
func example4ProtectedStruct() {
	fmt.Println("\n=== EXAMPLE 4: Protected Struct with Methods ===")

	type BankAccount struct {
		mu      sync.Mutex
		balance float64
	}

	// Method: Deposit (thread-safe)
	deposit := func(account *BankAccount, amount float64) {
		account.mu.Lock()
		defer account.mu.Unlock()
		account.balance += amount
		fmt.Printf("Deposited: %.2f, new balance: %.2f\n", amount, account.balance)
	}

	// Method: Withdraw (thread-safe)
	withdraw := func(account *BankAccount, amount float64) bool {
		account.mu.Lock()
		defer account.mu.Unlock()
		if account.balance >= amount {
			account.balance -= amount
			fmt.Printf("Withdrew: %.2f, new balance: %.2f\n", amount, account.balance)
			return true
		}
		fmt.Printf("Insufficient funds for withdrawal of %.2f\n", amount)
		return false
	}

	account := &BankAccount{balance: 100.0}

	// Concurrent transactions
	go deposit(account, 50)
	go withdraw(account, 30)
	go deposit(account, 20)
	go withdraw(account, 150) // Should fail

	time.Sleep(50 * time.Millisecond)
}

/*
EXAMPLE 5: Reader-Writer Scenario (Why RWMutex exists)
=====================================================
Regular Mutex blocks all access. RWMutex would be better if reads outnumber writes.
*/
func example5ReaderWriterScenario() {
	fmt.Println("\n=== EXAMPLE 5: Reader-Writer Scenario ===")

	type UserCache struct {
		mu    sync.Mutex
		users map[string]string
	}

	cache := &UserCache{users: make(map[string]string)}

	// Many readers
	for i := 0; i < 10; i++ {
		go func(id int) {
			cache.mu.Lock()
			defer cache.mu.Unlock()
			count := len(cache.users)
			fmt.Printf("Reader %d: checked cache, found %d users\n", id, count)
			time.Sleep(5 * time.Millisecond) // Simulate read operation
		}(i)
	}

	// Few writers
	for i := 0; i < 2; i++ {
		go func(id int) {
			cache.mu.Lock()
			defer cache.mu.Unlock()
			key := fmt.Sprintf("user%d", id)
			cache.users[key] = fmt.Sprintf("value%d", id)
			fmt.Printf("Writer %d: added user\n", id)
		}(i)
	}

	time.Sleep(200 * time.Millisecond)
	fmt.Println("Note: With Mutex, readers must wait for writers. RWMutex would allow concurrent reads.")
}

/*
EXAMPLE 6: Critical Section - Keep It Small
==========================================
Lock for the minimum time needed. Move non-critical operations outside the lock.
*/
func example6CriticalSectionSize() {
	fmt.Println("\n=== EXAMPLE 6: Keep Critical Section Small ===")

	type Logger struct {
		mu    sync.Mutex
		logs  []string
	}

	logger := &Logger{}

	for i := 0; i < 5; i++ {
		go func(id int) {
			// Expensive operation OUTSIDE critical section
			processedData := fmt.Sprintf("processed data for goroutine %d", id)

			// Only lock while accessing shared resource
			logger.mu.Lock()
			logger.logs = append(logger.logs, processedData)
			logger.mu.Unlock()
			// NOT holding lock, allowing other goroutines to proceed quickly
		}(i)
	}

	time.Sleep(50 * time.Millisecond)
	logger.mu.Lock()
	fmt.Printf("Total logs: %d\n", len(logger.logs))
	logger.mu.Unlock()
}

/*
EXAMPLE 7: TryLock - Non-blocking Attempt
=========================================
TryLock attempts to acquire lock without blocking (Go 1.18+).
Returns true if successful, false if lock is held.
*/
func example7TryLock() {
	fmt.Println("\n=== EXAMPLE 7: TryLock (Non-blocking) ===")

	type Resource struct {
		mu    sync.Mutex
		data  string
	}

	resource := &Resource{data: "initial"}

	// First goroutine holds the lock
	go func() {
		resource.mu.Lock()
		fmt.Println("Goroutine 1: acquired lock")
		resource.data = "modified by 1"
		time.Sleep(100 * time.Millisecond)
		resource.mu.Unlock()
		fmt.Println("Goroutine 1: released lock")
	}()

	time.Sleep(10 * time.Millisecond) // Let first goroutine get lock

	// Second goroutine tries non-blocking
	if resource.mu.TryLock() {
		fmt.Println("Goroutine 2: successfully acquired lock")
		resource.mu.Unlock()
	} else {
		fmt.Println("Goroutine 2: lock was held, doing something else instead")
	}

	time.Sleep(150 * time.Millisecond)
}

/*
EXAMPLE 8: Multiple Mutexes - Avoiding Deadlocks
================================================
Always lock multiple mutexes in the same order to prevent deadlocks.
*/
func example8MultipleLocksOrder() {
	fmt.Println("\n=== EXAMPLE 8: Multiple Locks - Order Matters ===")

	type Account struct {
		mu      sync.Mutex
		balance float64
	}

	accountA := &Account{balance: 100}
	accountB := &Account{balance: 50}

	// Transfer from A to B (always lock A first, then B)
	transfer := func(from, to *Account, amount float64) {
		// CRITICAL: Always lock in same order (from first, then to)
		from.mu.Lock()
		defer from.mu.Unlock()

		to.mu.Lock()
		defer to.mu.Unlock()

		if from.balance >= amount {
			from.balance -= amount
			to.balance += amount
			fmt.Printf("Transferred %.2f\n", amount)
		}
	}

	go transfer(accountA, accountB, 20)
	go transfer(accountB, accountA, 10)

	time.Sleep(50 * time.Millisecond)
	accountA.mu.Lock()
	accountB.mu.Lock()
	fmt.Printf("A: %.2f, B: %.2f\n", accountA.balance, accountB.balance)
	accountB.mu.Unlock()
	accountA.mu.Unlock()
}

/*
EXAMPLE 9: Atomic vs Mutex - Performance
========================================
For simple operations on single values, sync/atomic is faster than Mutex.
*/
func example9PerformanceComparison() {
	fmt.Println("\n=== EXAMPLE 9: Mutex for Complex Operations ===")

	type ComplexState struct {
		mu       sync.Mutex
		counter  int
		lastTime time.Time
		data     []int
	}

	state := &ComplexState{data: make([]int, 0)}

	for i := 0; i < 100; i++ {
		go func(id int) {
			state.mu.Lock()
			defer state.mu.Unlock()

			// Complex operation that needs atomicity
			state.counter++
			state.lastTime = time.Now()
			state.data = append(state.data, id)
		}(i)
	}

	time.Sleep(100 * time.Millisecond)
	state.mu.Lock()
	fmt.Printf("Counter: %d, Data length: %d\n", state.counter, len(state.data))
	state.mu.Unlock()
}

/*
EXAMPLE 10: Nested Function Calls - Lock Once
==============================================
When calling functions from inside a critical section, be aware of lock scope.
Avoid double-locking or missing locks.
*/
func example10NestedFunctionCalls() {
	fmt.Println("\n=== EXAMPLE 10: Nested Function Calls with Mutex ===")

	type Document struct {
		mu   sync.Mutex
		text string
	}

	// Safely append - assumes caller holds lock
	appendUnlocked := func(doc *Document, s string) {
		// This function assumes the lock is already held!
		doc.text += s
	}

	// Public method - acquires lock
	append := func(doc *Document, s string) {
		doc.mu.Lock()
		defer doc.mu.Unlock()
		appendUnlocked(doc, s)
	}

	doc := &Document{}

	for i := 0; i < 3; i++ {
		go func(id int) {
			append(doc, fmt.Sprintf(" [msg%d]", id))
		}(i)
	}

	time.Sleep(50 * time.Millisecond)
	doc.mu.Lock()
	fmt.Printf("Document: %s\n", doc.text)
	doc.mu.Unlock()
}

func main() {
	example1BasicMutex()
	example2MutexWithDefer()
	example3ProtectedMap()
	example4ProtectedStruct()
	example5ReaderWriterScenario()
	example6CriticalSectionSize()
	example7TryLock()
	example8MultipleLocksOrder()
	example9PerformanceComparison()
	example10NestedFunctionCalls()
}
