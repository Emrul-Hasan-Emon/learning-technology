package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {

	// 1️. BASIC RATE LIMITING (1 request every 500ms)
	fmt.Println("===== BASIC RATE LIMITING =====")

	// ticker emits a signal every 500ms
	limiter := time.Tick(500 * time.Millisecond)

	for i := 1; i <= 5; i++ {
		<-limiter // wait for permission
		fmt.Println("Request", i, "processed at", time.Now().Format("15:04:05"))
	}

	// 2️. BURST RATE LIMITING (Allow bursts + steady limit)
	fmt.Println("\n===== BURST RATE LIMITING =====")

	// Buffered channel allows bursts of 3 requests instantly
	burstLimiter := make(chan time.Time, 3)

	// Fill burst tokens
	for i := 0; i < 3; i++ {
		burstLimiter <- time.Now()
	}

	// Refill tokens at steady rate
	go func() {
		for t := range time.Tick(1 * time.Second) {
			burstLimiter <- t
		}
	}()

	for i := 1; i <= 6; i++ {
		<-burstLimiter
		fmt.Println("Burst request", i, "processed at", time.Now().Format("15:04:05"))
	}

	// 3️. WORKER POOL RATE LIMITING
	// Limit number of concurrent workers
	fmt.Println("\n===== WORKER POOL RATE LIMITING =====")

	jobs := make(chan int, 10)
	var wg sync.WaitGroup

	// Only 3 workers allowed concurrently
	for w := 1; w <= 3; w++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			for job := range jobs {
				fmt.Println("Worker", id, "processing job", job)
				time.Sleep(time.Second)
			}
		}(w)
	}

	for i := 1; i <= 8; i++ {
		jobs <- i
	}
	close(jobs)
	wg.Wait()

	// 4️. API REQUEST RATE LIMITING SIMULATION
	// Example: 5 requests per second allowed
	fmt.Println("\n===== API RATE LIMITING =====")

	apiLimiter := time.Tick(200 * time.Millisecond) // 5 req/sec

	for i := 1; i <= 10; i++ {
		go func(i int) {
			<-apiLimiter
			fmt.Println("API request", i, "served")
		}(i)
	}

	time.Sleep(3 * time.Second)

	// 5️. SHARED RESOURCE RATE LIMITING (DB / Memory access)
	// Limit concurrent access using Semaphore pattern
	fmt.Println("\n===== MEMORY/DB ACCESS LIMITING =====")

	semaphore := make(chan struct{}, 2) // Only 2 concurrent access allowed

	for i := 1; i <= 5; i++ {
		go func(i int) {

			// Acquire slot
			semaphore <- struct{}{}
			fmt.Println("Accessing DB:", i)

			time.Sleep(2 * time.Second)

			fmt.Println("Done DB:", i)

			// Release slot
			<-semaphore
		}(i)
	}

	time.Sleep(6 * time.Second)

	// 6️. PER USER RATE LIMITING (Token Bucket per user)
	fmt.Println("\n===== PER USER RATE LIMITING =====")

	userLimiters := make(map[string]chan time.Time)

	getLimiter := func(user string) chan time.Time {
		if limiter, exists := userLimiters[user]; exists {
			return limiter
		}

		limiter := make(chan time.Time, 2)

		// refill tokens
		go func() {
			for t := range time.Tick(1 * time.Second) {
				select {
				case limiter <- t:
				default:
				}
			}
		}()

		userLimiters[user] = limiter
		return limiter
	}

	users := []string{"Alice", "Bob"}

	for i := 1; i <= 5; i++ {
		for _, user := range users {
			go func(user string, req int) {
				<-getLimiter(user)
				fmt.Println(user, "request", req, "served")
			}(user, i)
		}
	}

	time.Sleep(6 * time.Second)

	fmt.Println("\nAll rate limiting examples finished 🚀")
}