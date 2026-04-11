package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

// -----------------------------
// Read request structure
// -----------------------------
type readOp struct {
	key  int
	resp chan int
}

// -----------------------------
// Write request structure
// -----------------------------
type writeOp struct {
	key  int
	val  int
	resp chan bool
}

func main() {

	fmt.Println("===== ACTOR MODEL (CHANNEL OWNED STATE) =====")

	// counters for performance tracking
	var readOps uint64
	var writeOps uint64

	// channels for requests
	reads := make(chan readOp)
	writes := make(chan writeOp)

	// 1️. SINGLE OWNER GOROUTINE (STATE CONTAINER)
	go func() {

		// ONLY this goroutine owns the map (NO mutex needed)
		state := make(map[int]int)

		for {
			select {

			// READ REQUEST
			case read := <-reads:
				read.resp <- state[read.key]

			// WRITE REQUEST
			case write := <-writes:
				state[write.key] = write.val
				write.resp <- true
			}
		}
	}()

	// 2️. MULTIPLE READER GOROUTINES
	for i := 0; i < 100; i++ {
		go func() {
			for {
				read := readOp{
					key:  rand.Intn(5),
					resp: make(chan int),
				}

				// send read request to state owner
				reads <- read

				// wait response
				<-read.resp

				atomic.AddUint64(&readOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// 3️. MULTIPLE WRITER GOROUTINES
	for i := 0; i < 10; i++ {
		go func() {
			for {
				write := writeOp{
					key:  rand.Intn(5),
					val:  rand.Intn(100),
					resp: make(chan bool),
				}

				// send write request
				writes <- write

				// wait confirmation
				<-write.resp

				atomic.AddUint64(&writeOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}

	// 4️. RUN SYSTEM FOR SOME TIME
	time.Sleep(time.Second)

	// 5️. PRINT STATS
	fmt.Println("readOps:", atomic.LoadUint64(&readOps))
	fmt.Println("writeOps:", atomic.LoadUint64(&writeOps))
}