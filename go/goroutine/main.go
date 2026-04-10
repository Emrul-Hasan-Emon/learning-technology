package main

import (
	"fmt"
	"sync"
	"time"
)

func f(from string) {
	for i := range 3 {
		fmt.Println(from, ":", i)
	}
}

func main() {

	// ---------------------------------------------------
	// 1. Normal (Synchronous call)
	// ---------------------------------------------------
	f("direct")

	// ---------------------------------------------------
	// 2. Basic Goroutine (async execution)
	// ---------------------------------------------------
	go f("goroutine-1")

	// ---------------------------------------------------
	// 3. Anonymous Goroutine
	// ---------------------------------------------------
	go func(msg string) {
		fmt.Println("anonymous:", msg)
	}("hello")

	// ---------------------------------------------------
	// 4. Multiple Goroutines (concurrent execution)
	// ---------------------------------------------------
	for i := 0; i < 3; i++ {
		go f(fmt.Sprintf("loop-goroutine-%d", i))
	}

	// ---------------------------------------------------
	// 5. WaitGroup (BEST PRACTICE instead of Sleep)
	// ---------------------------------------------------
	var wg sync.WaitGroup

	wg.Add(2)

	go func() {
		defer wg.Done()
		f("wg-1")
	}()

	go func() {
		defer wg.Done()
		f("wg-2")
	}()

	wg.Wait() // wait until all goroutines finish

	// ---------------------------------------------------
	// 6. Goroutine with Channel (sync + communication)
	// ---------------------------------------------------
	ch := make(chan string)

	go func() {
		ch <- "message from goroutine"
	}()

	msg := <-ch
	fmt.Println("received:", msg)

	// ---------------------------------------------------
	// 7. Buffered Channel (no immediate blocking)
	// ---------------------------------------------------
	bufCh := make(chan int, 2)

	bufCh <- 1
	bufCh <- 2

	fmt.Println("buffered:", <-bufCh)
	fmt.Println("buffered:", <-bufCh)

	// ---------------------------------------------------
	// 8. Worker Pool Pattern
	// ---------------------------------------------------
	jobs := make(chan int)
	results := make(chan int)

	// worker function
	worker := func(id int, jobs <-chan int, results chan<- int) {
		for j := range jobs {
			fmt.Println("worker", id, "processing", j)
			results <- j * 2
		}
	}

	// start workers
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	// send jobs
	go func() {
		for j := 1; j <= 5; j++ {
			jobs <- j
		}
		close(jobs)
	}()

	// collect results
	for i := 1; i <= 5; i++ {
		fmt.Println("result:", <-results)
	}

	// ---------------------------------------------------
	// 9. Select Statement (multiple channels)
	// ---------------------------------------------------
	ch1 := make(chan string)
	ch2 := make(chan string)

	go func() {
		time.Sleep(100 * time.Millisecond)
		ch1 <- "from ch1"
	}()

	go func() {
		time.Sleep(50 * time.Millisecond)
		ch2 <- "from ch2"
	}()

	for i := 0; i < 2; i++ {
		select {
		case msg1 := <-ch1:
			fmt.Println(msg1)
		case msg2 := <-ch2:
			fmt.Println(msg2)
		}
	}

	// ---------------------------------------------------
	// 10. Fan-out Pattern (multiple goroutines)
	// ---------------------------------------------------
	fanOutCh := make(chan int)

	for i := 0; i < 3; i++ {
		go func(id int) {
			for v := range fanOutCh {
				fmt.Println("fan-out worker", id, "got", v)
			}
		}(i)
	}

	for i := 0; i < 5; i++ {
		fanOutCh <- i
	}
	close(fanOutCh)

	// ---------------------------------------------------
	// 11. Fan-in Pattern (merge channels)
	// ---------------------------------------------------
	in1 := make(chan int)
	in2 := make(chan int)
	out := make(chan int)

	go func() {
		in1 <- 1
		in1 <- 2
		close(in1)
	}()

	go func() {
		in2 <- 3
		in2 <- 4
		close(in2)
	}()

	go func() {
		for v := range in1 {
			out <- v
		}
		for v := range in2 {
			out <- v
		}
		close(out)
	}()

	for v := range out {
		fmt.Println("fan-in:", v)
	}

	// ---------------------------------------------------
	// 12. Race Condition Example (BAD PRACTICE)
	// ---------------------------------------------------
	counter := 0

	for i := 0; i < 1000; i++ {
		go func() {
			counter++ // unsafe concurrent access
		}()
	}

	time.Sleep(time.Second)
	fmt.Println("counter (unsafe):", counter)

	// ---------------------------------------------------
	// 13. Fix Race Condition using Mutex
	// ---------------------------------------------------
	var mu sync.Mutex
	safeCounter := 0

	for i := 0; i < 1000; i++ {
		go func() {
			mu.Lock()
			safeCounter++
			mu.Unlock()
		}()
	}

	time.Sleep(time.Second)
	fmt.Println("counter (safe):", safeCounter)

	// ---------------------------------------------------
	// 14. Closing Channel
	// ---------------------------------------------------
	done := make(chan int)

	go func() {
		for i := 0; i < 3; i++ {
			done <- i
		}
		close(done)
	}()

	for v := range done {
		fmt.Println("closed channel:", v)
	}

	// ---------------------------------------------------
	// 15. Sleep (only for demo, NOT recommended in production)
	// ---------------------------------------------------
	time.Sleep(time.Second)
	fmt.Println("done")
}