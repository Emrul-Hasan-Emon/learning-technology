package main

import (
	"fmt"
	"time"
)

// 1. Worker function that signals completion

func worker(done chan bool) {

	fmt.Print("working...")

	// simulate long task
	time.Sleep(time.Second)

	fmt.Println("done")

	// signal completion to main goroutine
	done <- true
}

// 2. MAIN FUNCTION

func main() {

	// ---------------------------------------------------
	// 1. Basic Done Channel (your original pattern)
	// ---------------------------------------------------

	done := make(chan bool, 1)

	go worker(done)

	// block until worker sends signal
	<-done

	// ---------------------------------------------------
	// 2. Multiple Workers Sync (Wait using channels)
	// ---------------------------------------------------

	doneMulti := make(chan bool)

	for i := 1; i <= 3; i++ {
		go func(id int) {
			fmt.Println("worker", id, "started")
			time.Sleep(time.Second)
			fmt.Println("worker", id, "finished")

			doneMulti <- true
		}(i)
	}

	// wait for all workers
	for i := 0; i < 3; i++ {
		<-doneMulti
	}

	fmt.Println("all workers done")

	// ---------------------------------------------------
	// 3. Buffered Done Channel (avoid blocking sender)
	// ---------------------------------------------------

	doneBuf := make(chan bool, 2)

	go func() {
		time.Sleep(500 * time.Millisecond)
		doneBuf <- true
	}()

	go func() {
		time.Sleep(500 * time.Millisecond)
		doneBuf <- true
	}()

	<-doneBuf
	<-doneBuf

	fmt.Println("buffered workers done")

	// ---------------------------------------------------
	// 4. Done Channel with Result Communication
	// ---------------------------------------------------

	type result struct {
		id  int
		val int
	}

	resultCh := make(chan result)

	go func() {
		time.Sleep(500 * time.Millisecond)
		resultCh <- result{id: 1, val: 100}
	}()

	res := <-resultCh
	fmt.Println("received result:", res)

	// ---------------------------------------------------
	// 5. Done Channel with Timeout (Safety Pattern)
	// ---------------------------------------------------

	timeout := make(chan bool)

	go func() {
		time.Sleep(2 * time.Second)
		timeout <- true
	}()

	select {
	case <-timeout:
		fmt.Println("task finished")
	case <-time.After(1 * time.Second):
		fmt.Println("timeout reached")
	}

	// ---------------------------------------------------
	// 6. Fan-out style done signals
	// ---------------------------------------------------

	fanDone := make(chan bool)

	for i := 0; i < 3; i++ {
		go func(id int) {
			time.Sleep(300 * time.Millisecond)
			fmt.Println("fan worker done:", id)
			fanDone <- true
		}(i)
	}

	for i := 0; i < 3; i++ {
		<-fanDone
	}

	fmt.Println("fan-out complete")
}