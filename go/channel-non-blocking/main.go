package main

import (
	"fmt"
	"time"
)

func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		time.Sleep(time.Millisecond * 500)
		results <- j * 2
	}
}

func main() {

	fmt.Println("===== NON BLOCKING RECEIVE =====")
	messages := make(chan string)
	signals := make(chan bool)

	select {
	case msg := <-messages:
		fmt.Println("received message:", msg)
	default:
		fmt.Println("no message received (non-blocking)")
	}

	fmt.Println("\n===== NON BLOCKING SEND =====")
	msg := "hello"

	select {
	case messages <- msg:
		fmt.Println("sent message:", msg)
	default:
		fmt.Println("no receiver available → send skipped")
	}

	fmt.Println("\n===== NON BLOCKING MULTI CHANNEL SELECT =====")
	select {
	case msg := <-messages:
		fmt.Println("received message:", msg)
	case sig := <-signals:
		fmt.Println("received signal:", sig)
	default:
		fmt.Println("no activity")
	}

	// -------------------------------------------------------

	fmt.Println("\n===== ADD GOROUTINE PRODUCER =====")

	go func() {
		time.Sleep(time.Second)
		messages <- "async message"
		signals <- true
	}()

	time.Sleep(1500 * time.Millisecond)

	select {
	case msg := <-messages:
		fmt.Println("received:", msg)
	case sig := <-signals:
		fmt.Println("received signal:", sig)
	default:
		fmt.Println("still nothing")
	}

	// -------------------------------------------------------

	fmt.Println("\n===== SELECT WITH TIMEOUT =====")

	timeoutChan := make(chan string)
	go func() {
		time.Sleep(2 * time.Second)
		timeoutChan <- "finished work"
	}()

	select {
	case res := <-timeoutChan:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout! work too slow")
	}

	// -------------------------------------------------------

	fmt.Println("\n===== SELECT IN LOOP (EVENT LOOP STYLE) =====")

	eventChan := make(chan string)
	done := make(chan bool)

	go func() {
		for i := 1; i <= 3; i++ {
			time.Sleep(time.Second)
			eventChan <- fmt.Sprintf("event %d", i)
		}
		done <- true
	}()

loop:
	for {
		select {
		case e := <-eventChan:
			fmt.Println("event received:", e)
		case <-done:
			fmt.Println("all events processed")
			break loop
		case <-time.After(1500 * time.Millisecond):
			fmt.Println("waiting for events...")
		}
	}

	// -------------------------------------------------------

	fmt.Println("\n===== NON BLOCKING WORKER POOL CHECK =====")

	jobs := make(chan int, 3)
	results := make(chan int, 3)

	go worker(1, jobs, results)

	jobs <- 1
	jobs <- 2
	jobs <- 3
	close(jobs)

	for i := 0; i < 4; i++ {
		select {
		case r := <-results:
			fmt.Println("result:", r)
		default:
			fmt.Println("no result ready yet")
			time.Sleep(300 * time.Millisecond)
		}
	}

	fmt.Println("\nProgram finished 🚀")
}