package main

import (
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

func main() {

	// 1️. ATOMIC COUNTER (Most common use case)
	fmt.Println("===== ATOMIC COUNTER =====")

	var ops atomic.Uint64
	var wg sync.WaitGroup

	numWorkers := 50

	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()

			for j := 0; j < 1000; j++ {
				ops.Add(1) // atomic increment (thread-safe)
			}
		}()
	}

	wg.Wait()
	fmt.Println("Total operations:", ops.Load())

	// 2️. ATOMIC ADD & SUBTRACT
	fmt.Println("\n===== ATOMIC ADD / SUBTRACT =====")

	var balance atomic.Int64

	balance.Add(100) // deposit
	balance.Add(-30) // withdraw

	fmt.Println("Balance:", balance.Load())

	// 3️. COMPARE AND SWAP (CAS) — VERY IMPORTANT
	// Used for optimistic locking
	fmt.Println("\n===== COMPARE AND SWAP =====")

	var state atomic.Int32
	state.Store(0)

	swapped := state.CompareAndSwap(0, 1)

	fmt.Println("Was state changed?", swapped)
	fmt.Println("Current state:", state.Load())

	// Try swapping wrong value
	swapped = state.CompareAndSwap(0, 2)
	fmt.Println("Second swap success?", swapped)

	// 4️. ATOMIC BOOLEAN (Using Uint32)
	// Used as ON/OFF flag safely across goroutines
	fmt.Println("\n===== ATOMIC FLAG =====")

	var isRunning atomic.Bool

	isRunning.Store(true)

	go func() {
		time.Sleep(2 * time.Second)
		isRunning.Store(false)
	}()

	for isRunning.Load() {
		fmt.Println("Program running...")
		time.Sleep(500 * time.Millisecond)
	}
	fmt.Println("Program stopped")

	// 5️. ATOMIC VALUE (Store ANY type safely)
	// Great for config / cache updates
	fmt.Println("\n===== ATOMIC VALUE =====")

	var config atomic.Value

	// Store initial config
	config.Store(map[string]string{
		"env": "prod",
	})

	go func() {
		time.Sleep(2 * time.Second)

		// Update config safely
		config.Store(map[string]string{
			"env": "staging",
		})
	}()

	for i := 0; i < 3; i++ {
		currentConfig := config.Load().(map[string]string)
		fmt.Println("Current config:", currentConfig)
		time.Sleep(time.Second)
	}

	// 6️. ATOMIC vs MUTEX (Performance insight)
	fmt.Println("\n===== ATOMIC vs MUTEX =====")

	var counter atomic.Int64
	var mutex sync.Mutex
	var normalCounter int64

	// Atomic increment (lock-free)
	for i := 0; i < 1000; i++ {
		go counter.Add(1)
	}

	// Mutex increment (uses lock)
	for i := 0; i < 1000; i++ {
		go func() {
			mutex.Lock()
			normalCounter++
			mutex.Unlock()
		}()
	}

	time.Sleep(2 * time.Second)

	fmt.Println("Atomic counter:", counter.Load())
	fmt.Println("Mutex counter :", normalCounter)

	fmt.Println("\nAll atomic examples finished 🚀")
}