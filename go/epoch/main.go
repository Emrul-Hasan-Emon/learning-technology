package main

import (
	"fmt"
	"time"
)

func main() {

	fmt.Println("===== CURRENT TIME =====")
	now := time.Now()
	fmt.Println("Local:", now)
	fmt.Println("UTC:", now.UTC())

	// --------------------------------------------------
	// BASIC UNIX TIMESTAMPS
	// --------------------------------------------------
	fmt.Println("\n===== UNIX TIMESTAMPS =====")
	fmt.Println("Unix Seconds:", now.Unix())
	fmt.Println("Unix Milliseconds:", now.UnixMilli())
	fmt.Println("Unix Microseconds:", now.UnixMicro())
	fmt.Println("Unix Nanoseconds:", now.UnixNano())

	// --------------------------------------------------
	// CONVERT UNIX → TIME
	// --------------------------------------------------
	fmt.Println("\n===== UNIX → TIME CONVERSION =====")
	fromSeconds := time.Unix(now.Unix(), 0)
	fmt.Println("From Seconds:", fromSeconds)

	fromNano := time.Unix(0, now.UnixNano())
	fmt.Println("From Nanoseconds:", fromNano)

	fromMilli := time.UnixMilli(now.UnixMilli())
	fmt.Println("From Milliseconds:", fromMilli)

	fromMicro := time.UnixMicro(now.UnixMicro())
	fmt.Println("From Microseconds:", fromMicro)

	// --------------------------------------------------
	// CREATE CUSTOM UNIX TIMESTAMP
	// --------------------------------------------------
	fmt.Println("\n===== CUSTOM TIMESTAMP =====")
	custom := time.Unix(1700000000, 0)
	fmt.Println("Custom Unix Time:", custom)

	// --------------------------------------------------
	// FORMAT TIME INTO STRINGS
	// --------------------------------------------------
	fmt.Println("\n===== FORMATTING =====")
	fmt.Println("RFC3339:", now.Format(time.RFC3339))
	fmt.Println("RFC822:", now.Format(time.RFC822))
	fmt.Println("Kitchen:", now.Format(time.Kitchen))
	fmt.Println("Custom Format:", now.Format("2006-01-02 15:04:05"))

	// --------------------------------------------------
	// PARSE STRING → TIME
	// --------------------------------------------------
	fmt.Println("\n===== PARSING =====")
	dateStr := "2025-12-25 10:30:00"
	parsed, _ := time.Parse("2006-01-02 15:04:05", dateStr)
	fmt.Println("Parsed:", parsed)

	// Parse with timezone
	dateWithTZ := "2025-12-25T10:30:00+06:00"
	parsedTZ, _ := time.Parse(time.RFC3339, dateWithTZ)
	fmt.Println("Parsed with TZ:", parsedTZ)

	// --------------------------------------------------
	// TIME ZONE CONVERSION
	// --------------------------------------------------
	fmt.Println("\n===== TIME ZONES =====")
	loc, _ := time.LoadLocation("Asia/Dhaka")
	dhakaTime := now.In(loc)
	fmt.Println("Dhaka Time:", dhakaTime)

	nyLoc, _ := time.LoadLocation("America/New_York")
	fmt.Println("New York Time:", now.In(nyLoc))

	// --------------------------------------------------
	// DURATION OPERATIONS
	// --------------------------------------------------
	fmt.Println("\n===== DURATIONS =====")
	future := now.Add(48 * time.Hour)
	past := now.Add(-24 * time.Hour)

	fmt.Println("Future (+48h):", future)
	fmt.Println("Past (-24h):", past)

	duration := future.Sub(now)
	fmt.Println("Duration:", duration)
	fmt.Println("Hours:", duration.Hours())
	fmt.Println("Minutes:", duration.Minutes())
	fmt.Println("Seconds:", duration.Seconds())

	// --------------------------------------------------
	// TIME COMPARISON
	// --------------------------------------------------
	fmt.Println("\n===== COMPARISON =====")
	fmt.Println("future.After(now):", future.After(now))
	fmt.Println("past.Before(now):", past.Before(now))
	fmt.Println("now.Equal(now):", now.Equal(now))

	// --------------------------------------------------
	// TRUNCATE & ROUND TIME
	// --------------------------------------------------
	fmt.Println("\n===== ROUND & TRUNCATE =====")
	fmt.Println("Round to Hour:", now.Round(time.Hour))
	fmt.Println("Truncate to Hour:", now.Truncate(time.Hour))

	// --------------------------------------------------
	// SINCE & UNTIL
	// --------------------------------------------------
	fmt.Println("\n===== SINCE & UNTIL =====")
	start := time.Now()
	time.Sleep(2 * time.Second)
	fmt.Println("Time Since start:", time.Since(start))

	event := time.Now().Add(5 * time.Second)
	fmt.Println("Time Until event:", time.Until(event))

	// --------------------------------------------------
	// TIMERS
	// --------------------------------------------------
	fmt.Println("\n===== TIMER =====")
	timer := time.NewTimer(2 * time.Second)
	<-timer.C
	fmt.Println("Timer fired after 2 seconds")

	// --------------------------------------------------
	// TICKERS
	// --------------------------------------------------
	fmt.Println("\n===== TICKER (3 ticks) =====")
	ticker := time.NewTicker(1 * time.Second)
	count := 0
	for t := range ticker.C {
		fmt.Println("Tick at:", t)
		count++
		if count == 3 {
			ticker.Stop()
			break
		}
	}

	// --------------------------------------------------
	// DEADLINES & TIMEOUT EXAMPLE
	// --------------------------------------------------
	fmt.Println("\n===== TIMEOUT SIMULATION =====")
	timeout := time.After(2 * time.Second)

	select {
	case <-time.After(3 * time.Second):
		fmt.Println("Operation finished")
	case <-timeout:
		fmt.Println("Operation timed out!")
	}
}