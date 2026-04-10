package main

import (
	"fmt"
	"time"
)

func main() {

	// ---------------------------------------------------
	// 1. Basic Buffered Channel
	// ---------------------------------------------------
	messages := make(chan string, 2)

	messages <- "buffered"
	messages <- "channel"

	fmt.Println("receive 1:", <-messages)
	fmt.Println("receive 2:", <-messages)

	// ---------------------------------------------------
	// 2. Buffered Channel Capacity Behavior
	// ---------------------------------------------------
	buf := make(chan int, 3)

	fmt.Println("\nBuffer capacity demo")

	buf <- 1
	buf <- 2
	buf <- 3

	fmt.Println("values:", <-buf, <-buf, <-buf)

	// ---------------------------------------------------
	// 3. Blocking Behavior when Buffer is Full
	// ---------------------------------------------------
	block := make(chan int, 2)

	block <- 10
	block <- 20

	go func() {
		// this will wait until space is available
		block <- 30
		fmt.Println("sent 30")
	}()

	time.Sleep(1 * time.Second)

	fmt.Println("receive:", <-block)
	fmt.Println("receive:", <-block)
	fmt.Println("receive:", <-block)

	// ---------------------------------------------------
	// 4. Buffered Channel with Goroutines (Producer-Consumer)
	// ---------------------------------------------------
	jobs := make(chan int, 5)
	results := make(chan int, 5)

	go func() {
		for i := 1; i <= 5; i++ {
			jobs <- i
		}
		close(jobs)
	}()

	go func() {
		for j := range jobs {
			fmt.Println("processing:", j)
			results <- j * 2
		}
		close(results)
	}()

	for r := range results {
		fmt.Println("result:", r)
	}

	// ---------------------------------------------------
	// 5. Buffered Channel + Worker Pool
	// ---------------------------------------------------
	tasks := make(chan int, 10)

	for w := 1; w <= 3; w++ {
		go func(id int) {
			for t := range tasks {
				fmt.Println("worker", id, "task", t)
			}
		}(w)
	}

	for i := 1; i <= 5; i++ {
		tasks <- i
	}
	close(tasks)

	time.Sleep(1 * time.Second)

	// ---------------------------------------------------
	// 6. Non-blocking Send using Select
	// ---------------------------------------------------
	nonBlock := make(chan int, 1)

	nonBlock <- 100

	select {
	case nonBlock <- 200:
		fmt.Println("sent 200")
	default:
		fmt.Println("channel full, skipping send")
	}

	fmt.Println("value:", <-nonBlock)

	// ---------------------------------------------------
	// 7. Non-blocking Receive
	// ---------------------------------------------------
	select {
	case v := <-nonBlock:
		fmt.Println("received:", v)
	default:
		fmt.Println("no value available")
	}

	// ---------------------------------------------------
	// 8. Buffered Channel Range Loop
	// ---------------------------------------------------
	rangeCh := make(chan int, 3)

	rangeCh <- 1
	rangeCh <- 2
	rangeCh <- 3
	close(rangeCh)

	fmt.Println("\nrange over buffered channel")
	for v := range rangeCh {
		fmt.Println(v)
	}

	// ---------------------------------------------------
	// 9. Buffered Channel Deadlock Case (Important)
	// ---------------------------------------------------
	// Uncommenting below will cause DEADLOCK if no receiver
	/*
		dead := make(chan int, 1)
		dead <- 1
		dead <- 2 // ❌ blocks here (buffer full)
	*/

	// ---------------------------------------------------
	// 10. Buffered Channel with Timeout
	// ---------------------------------------------------
	timeoutCh := make(chan string, 1)

	go func() {
		time.Sleep(2 * time.Second)
		timeoutCh <- "done"
	}()

	select {
	case msg := <-timeoutCh:
		fmt.Println("received:", msg)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout!")
	}

	// ---------------------------------------------------
	// 11. Buffered Channel as Queue (Real-world usage)
	// ---------------------------------------------------
	queue := make(chan string, 3)

	queue <- "task-1"
	queue <- "task-2"
	queue <- "task-3"

	fmt.Println("\nqueue processing:")
	for len(queue) > 0 {
		fmt.Println(<-queue)
	}
}