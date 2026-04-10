package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {

	// ---------------------------------------------------
	// 1. Basic Unbuffered Channel (Sync communication)
	// ---------------------------------------------------
	messages := make(chan string)

	go func() {
		messages <- "ping" // send
	}()

	msg := <-messages // receive
	fmt.Println("basic:", msg)

	// ---------------------------------------------------
	// 2. Buffered Channel (Async send)
	// ---------------------------------------------------
	buf := make(chan int, 2)

	buf <- 1
	buf <- 2

	fmt.Println("buffered:", <-buf)
	fmt.Println("buffered:", <-buf)

	// ---------------------------------------------------
	// 3. Channel Blocking Behavior
	// ---------------------------------------------------
	block := make(chan string)

	go func() {
		time.Sleep(1 * time.Second)
		block <- "done after delay"
	}()

	fmt.Println("blocking:", <-block)

	// ---------------------------------------------------
	// 4. Channel with Multiple Goroutines (Producer-Consumer)
	// ---------------------------------------------------
	jobs := make(chan int)
	results := make(chan int)

	// worker goroutines
	for w := 1; w <= 3; w++ {
		go func(id int) {
			for j := range jobs {
				fmt.Println("worker", id, "processing", j)
				results <- j * 2
			}
		}(w)
	}

	// send jobs
	go func() {
		for i := 1; i <= 5; i++ {
			jobs <- i
		}
		close(jobs) // IMPORTANT: close channel after sending
	}()

	// collect results
	go func() {
		for i := 1; i <= 5; i++ {
			fmt.Println("result:", <-results)
		}
	}()

	time.Sleep(time.Second)

	// ---------------------------------------------------
	// 5. Range over Channel
	// ---------------------------------------------------
	ch := make(chan int)

	go func() {
		for i := 1; i <= 3; i++ {
			ch <- i
		}
		close(ch)
	}()

	for v := range ch {
		fmt.Println("range:", v)
	}

	// ---------------------------------------------------
	// 6. Select (multiple channel handling)
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
		case msg := <-ch1:
			fmt.Println("select:", msg)
		case msg := <-ch2:
			fmt.Println("select:", msg)
		}
	}

	// ---------------------------------------------------
	// 7. Select with Timeout
	// ---------------------------------------------------
	timeout := make(chan string)

	go func() {
		time.Sleep(2 * time.Second)
		timeout <- "late response"
	}()

	select {
	case res := <-timeout:
		fmt.Println("received:", res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout occurred")
	}

	// ---------------------------------------------------
	// 8. Channel Direction (Send-only / Receive-only)
	// ---------------------------------------------------
	chDir := make(chan int)

	go sendOnly(chDir)
	go receiveOnly(chDir)

	time.Sleep(time.Second)

	// ---------------------------------------------------
	// 9. Closing Channel + Detection
	// ---------------------------------------------------
	done := make(chan int)

	go func() {
		for i := 0; i < 3; i++ {
			done <- i
		}
		close(done)
	}()

	for {
		v, ok := <-done
		if !ok {
			fmt.Println("channel closed")
			break
		}
		fmt.Println("value:", v)
	}

	// ---------------------------------------------------
	// 10. Fan-in Pattern (merge channels)
	// ---------------------------------------------------
	a := make(chan int)
	b := make(chan int)
	out := make(chan int)

	go func() {
		a <- 1
		a <- 2
		close(a)
	}()

	go func() {
		b <- 3
		b <- 4
		close(b)
	}()

	go func() {
		for v := range a {
			out <- v
		}
		for v := range b {
			out <- v
		}
		close(out)
	}()

	for v := range out {
		fmt.Println("fan-in:", v)
	}

	// ---------------------------------------------------
	// 11. Fan-out Pattern (multiple workers)
	// ---------------------------------------------------
	fan := make(chan int)

	for i := 0; i < 3; i++ {
		go func(id int) {
			for v := range fan {
				fmt.Println("worker", id, "got", v)
			}
		}(i)
	}

	for i := 0; i < 5; i++ {
		fan <- i
	}
	close(fan)

	// ---------------------------------------------------
	// 12. WaitGroup + Channel (proper sync)
	// ---------------------------------------------------
	var wg sync.WaitGroup
	task := make(chan int)

	wg.Add(2)

	go func() {
		defer wg.Done()
		for v := range task {
			fmt.Println("wg worker 1:", v)
		}
	}()

	go func() {
		defer wg.Done()
		for v := range task {
			fmt.Println("wg worker 2:", v)
		}
	}()

	go func() {
		for i := 0; i < 5; i++ {
			task <- i
		}
		close(task)
	}()

	wg.Wait()

	// ---------------------------------------------------
	// 13. Nil Channel (blocks forever)
	// ---------------------------------------------------
	var nilCh chan int

	// Uncommenting this will deadlock
	// nilCh <- 1

	fmt.Println("nil channel:", nilCh)
}

// Channel Direction Functions

func sendOnly(ch chan<- int) {
	ch <- 100
	fmt.Println("sent to channel")
}

func receiveOnly(ch <-chan int) {
	val := <-ch
	fmt.Println("received:", val)
}