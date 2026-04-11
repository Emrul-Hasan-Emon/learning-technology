package main

import (
	"fmt"
	"sync"
	"time"
)

// Worker function simulates a task
func worker(id int) {
	fmt.Printf("Worker %d starting\n", id)

	// Simulate work
	time.Sleep(time.Second)

	fmt.Printf("Worker %d done\n", id)
}

func main() {

	// WaitGroup is used to wait for multiple goroutines to finish.
	var wg sync.WaitGroup

	numWorkers := 5

	// Launch multiple goroutines
	for i := 1; i <= numWorkers; i++ {

		// IMPORTANT: Tell WaitGroup how many goroutines we will wait for
		wg.Add(1)

		// Start goroutine
		go func(id int) {
			// IMPORTANT: Mark goroutine as done when finished
			defer wg.Done()

			worker(id)

		}(i) // pass i as parameter (avoid closure bug)
	}

	// Wait until all goroutines call Done()
	wg.Wait()

	fmt.Println("All workers finished 🚀")
}