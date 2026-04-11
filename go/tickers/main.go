package main

import (
	"fmt"
	"time"
)

func main() {

	// BASIC TIMER
	// Creates a timer that fires once after 2 seconds.
	fmt.Println("===== BASIC TIMER =====")
	timer1 := time.NewTimer(2 * time.Second)

	// Timer sends a signal on timer.C channel when it fires.
	<-timer1.C
	fmt.Println("Timer 1 fired")

	// -----------------------------------------------------

	// STOPPING A TIMER BEFORE FIRING
	fmt.Println("\n===== STOPPING A TIMER BEFORE FIRING =====")
	timer2 := time.NewTimer(2 * time.Second)

	// Goroutine waiting for timer to fire
	go func() {
		<-timer2.C
		fmt.Println("Timer 2 fired")
	}()

	// Stop the timer before it fires
	stop2 := timer2.Stop()

	// Stop() returns true if successfully stopped before firing
	if stop2 {
		fmt.Println("Timer 2 stopped before firing")
	}

	time.Sleep(1 * time.Second)

	// -----------------------------------------------------

	// RESETTING A TIMER
	fmt.Println("\n===== RESETTING A TIMER =====")
	timer3 := time.NewTimer(1 * time.Second)

	<-timer3.C
	fmt.Println("Timer 3 fired first time")

	// Reset timer to fire again after 2 seconds
	timer3.Reset(2 * time.Second)

	<-timer3.C
	fmt.Println("Timer 3 fired after reset")

	// -----------------------------------------------------

	// TIMER vs time.Sleep
	fmt.Println("\n===== TIMER vs time.Sleep =====")

	start := time.Now()
	time.Sleep(1 * time.Second)
	fmt.Println("Sleep took:", time.Since(start))

	// time.After returns a channel that fires once after duration
	start = time.Now()
	<-time.After(1 * time.Second)
	fmt.Println("time.After took:", time.Since(start))

	// -----------------------------------------------------

	// MULTIPLE TIMERS WITH SELECT
	fmt.Println("\n===== MULTIPLE TIMERS WITH SELECT =====")

	c1 := time.After(1 * time.Second)
	c2 := time.After(2 * time.Second)

	// Waits whichever timer fires first
	select {
	case <-c1:
		fmt.Println("c1 fired first")
	case <-c2:
		fmt.Println("c2 fired first")
	}

	// -----------------------------------------------------

	// TIMEOUT PATTERN (VERY IMPORTANT IN REAL SYSTEMS)
	fmt.Println("\n===== TIMEOUT PATTERN =====")

	result := make(chan string)

	// Simulate slow background job
	go func() {
		time.Sleep(2 * time.Second)
		result <- "slow task finished"
	}()

	// Wait for result OR timeout
	select {
	case res := <-result:
		fmt.Println(res)
	case <-time.After(1 * time.Second):
		fmt.Println("timeout! task too slow")
	}

	// -----------------------------------------------------

	// TICKER (REPEATING TIMER)
	fmt.Println("\n===== TICKER =====")

	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			// Fires repeatedly every 500ms
			case t := <-ticker.C:
				fmt.Println("tick at", t.Format("15:04:05"))

			// Stop signal
			case <-done:
				fmt.Println("Ticker stopped")
				return
			}
		}
	}()

	time.Sleep(2 * time.Second)

	// Always stop ticker to prevent memory leak
	ticker.Stop()
	done <- true

	// -----------------------------------------------------

	// HEARTBEAT PATTERN (Used in servers & distributed systems)
	fmt.Println("\n===== HEARTBEAT PATTERN =====")

	heartbeat := time.NewTicker(1 * time.Second)

	go func() {
		// Range over ticker channel until stopped
		for t := range heartbeat.C {
			fmt.Println("heartbeat at", t.Format("15:04:05"))
		}
	}()

	time.Sleep(3 * time.Second)

	// Stop heartbeat
	heartbeat.Stop()

	fmt.Println("\nProgram finished 🚀")
}