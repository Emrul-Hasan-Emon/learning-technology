package main

import (
	"fmt"
	"time"
)

func main() {

	fmt.Println("===== BASIC TIMER =====")
	timer1 := time.NewTimer(2 * time.Second)
	<-timer1.C
	fmt.Println("Timer 1 fired")

	// -----------------------------------------------------

	fmt.Println("\n===== STOPPING A TIMER BEFORE FIRING =====")
	timer2 := time.NewTimer(2 * time.Second)

	go func() {
		<-timer2.C
		fmt.Println("Timer 2 fired")
	}()

	stop2 := timer2.Stop()
	if stop2 {
		fmt.Println("Timer 2 stopped before firing")
	}

	time.Sleep(1 * time.Second)

	// -----------------------------------------------------

	fmt.Println("\n===== RESETTING A TIMER =====")
	timer3 := time.NewTimer(1 * time.Second)
	<-timer3.C
	fmt.Println("Timer 3 fired first time")

	timer3.Reset(2 * time.Second)
	<-timer3.C
	fmt.Println("Timer 3 fired after reset")

	// -----------------------------------------------------

	fmt.Println("\n===== TIMER vs time.Sleep =====")
	start := time.Now()
	time.Sleep(1 * time.Second)
	fmt.Println("Sleep took:", time.Since(start))

	start = time.Now()
	<-time.After(1 * time.Second)
	fmt.Println("time.After took:", time.Since(start))

	// -----------------------------------------------------

	fmt.Println("\n===== MULTIPLE TIMERS WITH SELECT =====")
	c1 := time.After(1 * time.Second)
	c2 := time.After(2 * time.Second)

	select {
	case <-c1:
		fmt.Println("c1 fired first")
	case <-c2:
		fmt.Println("c2 fired first")
	}

	// -----------------------------------------------------

	fmt.Println("\n===== TIMEOUT PATTERN (VERY IMPORTANT) =====")
	result := make(chan string)

	go func() {
		time.Sleep(2 * time.Second)
		result <- "slow task finished"
	}()

	select {
	case res := <-result:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout! task too slow")
	}

	// -----------------------------------------------------

	fmt.Println("\n===== TICKER (REPEATING TIMER) =====")
	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			case t := <-ticker.C:
				fmt.Println("tick at", t.Format("15:04:05"))
			case <-done:
				fmt.Println("Ticker stopped")
				return
			}
		}
	}()

	time.Sleep(2 * time.Second)
	ticker.Stop()
	done <- true

	// -----------------------------------------------------

	fmt.Println("\n===== HEARTBEAT PATTERN =====")
	heartbeat := time.NewTicker(1 * time.Second)

	go func() {
		for t := range heartbeat.C {
			fmt.Println("heartbeat at", t.Format("15:04:05"))
		}
	}()

	time.Sleep(3 * time.Second)
	heartbeat.Stop()

	fmt.Println("\nProgram finished 🚀")
}