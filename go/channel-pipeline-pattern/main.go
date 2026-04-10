package main

import "fmt"

// 1. SEND-ONLY CHANNEL FUNCTION

// pings is send-only channel (chan<- string)
// This function can ONLY send data into the channel
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// 2. RECEIVE + SEND CHANNEL FUNCTION (Pipeline step)

// pings is receive-only (<-chan string)
// pongs is send-only (chan<- string)
//
// This enforces strict pipeline behavior:
// input → process → output
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

// 3. MAIN FUNCTION

func main() {

	// ---------------------------------------------------
	// 1. Basic pipeline using directional channels
	// ---------------------------------------------------

	pings := make(chan string, 1)
	pongs := make(chan string, 1)

	ping(pings, "passed message")
	pong(pings, pongs)

	fmt.Println("result:", <-pongs)

	// ---------------------------------------------------
	// 2. Multiple messages pipeline
	// ---------------------------------------------------

	pings2 := make(chan string, 3)
	pongs2 := make(chan string, 3)

	go func() {
		ping(pings2, "msg-1")
		ping(pings2, "msg-2")
		ping(pings2, "msg-3")
		close(pings2)
	}()

	go func() {
		for msg := range pings2 {
			pongs2 <- msg + " processed"
		}
		close(pongs2)
	}()

	for res := range pongs2 {
		fmt.Println("pipeline:", res)
	}

	// ---------------------------------------------------
	// 3. Fan-out pipeline (multiple workers)
	// ---------------------------------------------------

	input := make(chan int)
	output := make(chan int)

	// worker pool
	for i := 0; i < 3; i++ {
		go func(id int, in <-chan int, out chan<- int) {
			for v := range in {
				fmt.Println("worker", id, "processing", v)
				out <- v * 2
			}
		}(i, input, output)
	}

	// send data
	go func() {
		for i := 1; i <= 5; i++ {
			input <- i
		}
		close(input)
	}()

	// collect results
	go func() {
		for i := 1; i <= 5; i++ {
			fmt.Println("output:", <-output)
		}
	}()

	// allow goroutines to finish (demo only)
	select {}
}