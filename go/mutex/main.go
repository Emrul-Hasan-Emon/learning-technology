package main

import (
	"fmt"
	"sync"
)

// Container holds shared state
// Mutex protects map from concurrent writes
type Container struct {
	mu       sync.Mutex
	counters map[string]int
}

// inc safely increments a counter
func (c *Container) inc(name string) {
	c.mu.Lock()
	defer c.mu.Unlock()

	// critical section (only one goroutine at a time)
	c.counters[name]++
}

func main() {

	fmt.Println("===== BASIC MUTEX COUNTER =====")

	c := Container{
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	// helper function
	doIncrement := func(name string, n int) {
		defer wg.Done()

		for i := 0; i < n; i++ {
			c.inc(name)
		}
	}

	// launch goroutines safely
	wg.Add(3)

	go doIncrement("a", 10000)
	go doIncrement("a", 10000)
	go doIncrement("b", 10000)

	wg.Wait()

	fmt.Println("final counters:", c.counters)

	// 2️. READ + WRITE PROTECTION (Mutex protects map reads too)
	fmt.Println("\n===== SAFE READ + WRITE =====")

	type SafeMap struct {
		mu sync.Mutex
		m  map[string]int
	}

	sm := SafeMap{
		m: map[string]int{"x": 1},
	}

	var wg2 sync.WaitGroup

	// writer
	wg2.Add(1)
	go func() {
		defer wg2.Done()
		for i := 0; i < 1000; i++ {
			sm.mu.Lock()
			sm.m["x"]++
			sm.mu.Unlock()
		}
	}()

	// reader
	wg2.Add(1)
	go func() {
		defer wg2.Done()
		for i := 0; i < 10; i++ {
			sm.mu.Lock()
			fmt.Println("read:", sm.m["x"])
			sm.mu.Unlock()
		}
	}()

	wg2.Wait()

	// 3️. DEADLOCK EXAMPLE (IMPORTANT TO UNDERSTAND)
	fmt.Println("\n===== DEADLOCK AVOIDANCE =====")

	type Bank struct {
		mu      sync.Mutex
		balance int
	}

	b := Bank{balance: 100}

	// WRONG pattern would be double locking or missing unlock
	// Correct pattern:
	b.mu.Lock()
	b.balance += 50
	b.mu.Unlock()

	fmt.Println("bank balance:", b.balance)

	// 4️. MULTIPLE GOROUTINES SAFE ACCESS
	fmt.Println("\n===== HIGH CONCURRENCY SAFE ACCESS =====")

	type Counter struct {
		mu sync.Mutex
		v  int
	}

	counter := Counter{}

	var wg3 sync.WaitGroup

	for i := 0; i < 100; i++ {
		wg3.Add(1)

		go func() {
			defer wg3.Done()

			for j := 0; j < 100; j++ {
				counter.mu.Lock()
				counter.v++
				counter.mu.Unlock()
			}
		}()
	}

	wg3.Wait()

	fmt.Println("final counter value:", counter.v)
}