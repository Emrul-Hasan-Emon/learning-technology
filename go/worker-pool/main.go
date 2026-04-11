package main

import (
	"fmt"
	"time"
)

// Worker function
// id → worker number
// jobs → read-only channel (worker receives jobs)
// results → write-only channel (worker sends results)
func worker(id int, jobs <-chan int, results chan<- int) {

	// range over channel until it is closed
	for j := range jobs {

		fmt.Println("worker", id, "started job", j)

		// simulate heavy work
		time.Sleep(time.Second)

		fmt.Println("worker", id, "finished job", j)

		// send result back
		results <- j * 2
	}

	// When jobs channel is closed and drained, loop ends.
	fmt.Println("worker", id, "exiting")
}

func main() {

	const numJobs = 5
	const numWorkers = 3

	// Buffered channel → holds all jobs
	jobs := make(chan int, numJobs)

	// Buffered results channel → stores all results
	results := make(chan int, numJobs)

	// Start worker goroutines (Worker Pool)
	for w := 1; w <= numWorkers; w++ {
		go worker(w, jobs, results)
	}

	// Send jobs to workers
	for j := 1; j <= numJobs; j++ {
		fmt.Println("sending job", j)
		jobs <- j
	}

	// Close jobs channel to signal no more jobs
	close(jobs)

	// Collect results
	for a := 1; a <= numJobs; a++ {
		res := <-results
		fmt.Println("result received:", res)
	}

	fmt.Println("All jobs completed 🚀")
}