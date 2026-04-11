package main

import (
	"fmt"
	"time"
)

func worker(name string, delay time.Duration, out chan<- string) {
	time.Sleep(delay)
	out <- name
}

func main() {

	// channels
	c1 := make(chan string)
	c2 := make(chan string)
	done := make(chan bool)

	// producers
	go worker("fast worker", 1*time.Second, c1)
	go worker("slow worker", 3*time.Second, c2)

	// non-blocking check (default case)
	select {
	case msg := <-c1:
		fmt.Println("received early:", msg)
	default:
		fmt.Println("no message yet (non-blocking check)")
	}

	fmt.Println("---- waiting with select + timeout ----")

	// looped select with timeout + multiple channels
	go func() {
		for i := 0; i < 2; i++ {
			select {
			case msg1 := <-c1:
				fmt.Println("received from c1:", msg1)

			case msg2 := <-c2:
				fmt.Println("received from c2:", msg2)

			case <-time.After(2 * time.Second):
				fmt.Println("timeout while waiting")
			}
		}
		done <- true
	}()

	<-done

	fmt.Println("---- second timeout example ----")

	// Individual timeout example (like your previous code)
	c3 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c3 <- "result 1"
	}()

	select {
	case res := <-c3:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout 1")
	}

	c4 := make(chan string, 1)
	go func() {
		time.Sleep(2 * time.Second)
		c4 <- "result 2"
	}()

	select {
	case res := <-c4:
		fmt.Println(res)
	case <-time.After(3 * time.Second):
		fmt.Println("timeout 2")
	}

	fmt.Println("program finished")
}