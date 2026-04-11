package main

import (
	"fmt"
	"time"
)

func main() {

	// -----------------------------------------------------
	// 1️. CURRENT TIME
	// -----------------------------------------------------
	fmt.Println("===== CURRENT TIME =====")

	now := time.Now()
	fmt.Println("Now:", now)

	// UTC vs Local
	fmt.Println("Local:", now.Local())
	fmt.Println("UTC:", now.UTC())

	// Unix timestamps
	fmt.Println("Unix seconds:", now.Unix())
	fmt.Println("Unix milli :", now.UnixMilli())
	fmt.Println("Unix nano  :", now.UnixNano())

	// -----------------------------------------------------
	// 2️. CREATE SPECIFIC DATE
	// -----------------------------------------------------
	fmt.Println("\n===== CREATE SPECIFIC DATE =====")

	then := time.Date(
		2009, 11, 17, // year, month, day
		20, 34, 58,   // hour, minute, second
		651387237,    // nanoseconds
		time.UTC,     // timezone
	)

	fmt.Println("Custom date:", then)

	// Access parts
	fmt.Println("Year:", then.Year())
	fmt.Println("Month:", then.Month())
	fmt.Println("Day:", then.Day())
	fmt.Println("Hour:", then.Hour())
	fmt.Println("Minute:", then.Minute())
	fmt.Println("Second:", then.Second())
	fmt.Println("Nanosecond:", then.Nanosecond())
	fmt.Println("Weekday:", then.Weekday())

	// -----------------------------------------------------
	// 3️. TIME COMPARISON
	// -----------------------------------------------------
	fmt.Println("\n===== TIME COMPARISON =====")

	fmt.Println("then.Before(now):", then.Before(now))
	fmt.Println("then.After(now):", then.After(now))
	fmt.Println("then.Equal(now):", then.Equal(now))

	// -----------------------------------------------------
	// 4️. DURATION (TIME DIFFERENCE)
	// -----------------------------------------------------
	fmt.Println("\n===== DURATION =====")

	diff := now.Sub(then)
	fmt.Println("Duration:", diff)

	fmt.Println("Hours:", diff.Hours())
	fmt.Println("Minutes:", diff.Minutes())
	fmt.Println("Seconds:", diff.Seconds())

	// Add/Subtract duration
	fmt.Println("Add duration:", then.Add(diff))
	fmt.Println("Subtract duration:", then.Add(-diff))

	// -----------------------------------------------------
	// 5️. TIME ADD & SUBTRACT
	// -----------------------------------------------------
	fmt.Println("\n===== ADD / SUBTRACT TIME =====")

	fmt.Println("After 24 hours:", now.Add(24*time.Hour))
	fmt.Println("After 30 minutes:", now.Add(30*time.Minute))
	fmt.Println("Before 7 days:", now.AddDate(0, 0, -7))

	// AddDate(years, months, days)
	fmt.Println("After 1 year:", now.AddDate(1, 0, 0))
	fmt.Println("After 3 months:", now.AddDate(0, 3, 0))

	// -----------------------------------------------------
	// 6️. TIME FORMATTING (VERY IMPORTANT)
	// Go uses reference date: Mon Jan 2 15:04:05 2006
	// -----------------------------------------------------
	fmt.Println("\n===== FORMATTING =====")

	fmt.Println(now.Format("2006-01-02"))
	fmt.Println(now.Format("02-01-2006"))
	fmt.Println(now.Format("2006-01-02 15:04:05"))
	fmt.Println(now.Format(time.RFC3339))
	fmt.Println(now.Format(time.RFC822))
	fmt.Println(now.Format("03:04 PM"))

	// Custom human readable
	fmt.Println(now.Format("Monday, Jan 2 2006"))

	// -----------------------------------------------------
	// 7️. PARSING STRING → TIME
	// -----------------------------------------------------
	fmt.Println("\n===== PARSING =====")

	t1, _ := time.Parse("2006-01-02", "2024-03-15")
	fmt.Println("Parsed:", t1)

	t2, _ := time.Parse(time.RFC3339, "2024-03-15T14:30:00Z")
	fmt.Println("Parsed RFC3339:", t2)

	// Parse with timezone
	t3, _ := time.Parse("2006-01-02 15:04 MST",
		"2024-03-15 10:00 UTC")
	fmt.Println("Parsed with zone:", t3)

	// -----------------------------------------------------
	// 8️. TIME ZONES 🌍
	// -----------------------------------------------------
	fmt.Println("\n===== TIME ZONES =====")

	locNY, _ := time.LoadLocation("America/New_York")
	locTokyo, _ := time.LoadLocation("Asia/Tokyo")

	fmt.Println("New York:", now.In(locNY))
	fmt.Println("Tokyo:", now.In(locTokyo))

	// -----------------------------------------------------
	// 9️. SLEEP (PAUSE EXECUTION)
	// -----------------------------------------------------
	fmt.Println("\n===== SLEEP =====")

	fmt.Println("Sleeping 1 second...")
	time.Sleep(1 * time.Second)
	fmt.Println("Awake!")

	// -----------------------------------------------------
	// 10. MEASURE EXECUTION TIME (IMPORTANT)
	// -----------------------------------------------------
	fmt.Println("\n===== BENCHMARK / MEASURE TIME =====")

	start := time.Now()

	time.Sleep(500 * time.Millisecond) // simulate work

	elapsed := time.Since(start)
	fmt.Println("Task took:", elapsed)

	// -----------------------------------------------------
	// 11. START OF DAY / END OF DAY
	// -----------------------------------------------------
	fmt.Println("\n===== START / END OF DAY =====")

	y, m, d := now.Date()
	startOfDay := time.Date(y, m, d, 0, 0, 0, 0, now.Location())
	endOfDay := startOfDay.Add(24*time.Hour - time.Nanosecond)

	fmt.Println("Start of day:", startOfDay)
	fmt.Println("End of day:", endOfDay)

	// -----------------------------------------------------
	// 12. NEXT WEEKDAY EXAMPLE
	// -----------------------------------------------------
	fmt.Println("\n===== NEXT MONDAY =====")

	nextMonday := now
	for nextMonday.Weekday() != time.Monday {
		nextMonday = nextMonday.AddDate(0, 0, 1)
	}
	fmt.Println("Next Monday:", nextMonday)

	fmt.Println("\nProgram finished 🚀")
}