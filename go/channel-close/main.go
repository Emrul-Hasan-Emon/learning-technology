package main

import (
	"fmt"
	"time"
)

func worker(id int, jobs <-chan int, done chan<- bool) {
	for j := range jobs { // auto exits when channel closes
		fmt.Printf("worker %d received job %d\n", id, j)
		time.Sleep(time.Millisecond * 500)
	}
	fmt.Printf("worker %d: no more jobs\n", id)
	done <- true
}

func safeSend(ch chan int, val int) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("panic caught → cannot send to closed channel")
		}
	}()
	ch <- val
}

func main() {

	fmt.Println("===== BASIC CLOSE + DETECT =====")
	jobs := make(chan int, 5)
	done := make(chan bool)

	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	<-done

	_, ok := <-jobs
	fmt.Println("reading after close → ok:", ok)

	// -----------------------------------------------------

	fmt.Println("\n===== RANGE OVER CLOSED CHANNEL =====")
	nums := make(chan int, 3)
	nums <- 1
	nums <- 2
	nums <- 3
	close(nums)

	for n := range nums {
		fmt.Println("range read:", n)
	}

	// -----------------------------------------------------

	fmt.Println("\n===== MULTIPLE WORKERS DETECT CLOSE =====")
	jobQueue := make(chan int, 5)
	workerDone := make(chan bool)

	for w := 1; w <= 3; w++ {
		go worker(w, jobQueue, workerDone)
	}

	for j := 1; j <= 5; j++ {
		jobQueue <- j
	}
	close(jobQueue)

	for i := 0; i < 3; i++ {
		<-workerDone
	}

	// -----------------------------------------------------

	fmt.Println("\n===== BROADCAST SHUTDOWN VIA CLOSE =====")
	stop := make(chan struct{})

	for i := 1; i <= 3; i++ {
		go func(id int) {
			for {
				select {
				case <-stop:
					fmt.Println("goroutine", id, "stopped")
					return
				default:
					fmt.Println("goroutine", id, "working")
					time.Sleep(300 * time.Millisecond)
				}
			}
		}(i)
	}

	time.Sleep(time.Second)
	close(stop) // broadcast signal
	time.Sleep(time.Second)

	// -----------------------------------------------------

	fmt.Println("\n===== PANIC IF SENDING TO CLOSED CHANNEL =====")
	test := make(chan int)
	close(test)

	safeSend(test, 1)

	fmt.Println("\nProgram finished 🚀")
}