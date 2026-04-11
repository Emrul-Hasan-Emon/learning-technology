package main

import (
	"fmt"
	"time"
)

func main() {

	p := fmt.Println

	// ------------------------------------------------------------
	// 1️. CURRENT TIME
	// ------------------------------------------------------------
	fmt.Println("===== CURRENT TIME =====")

	t := time.Now()
	p("Now (default):", t)

	// ------------------------------------------------------------
	// 2️. RFC3339 FORMAT (MOST USED IN APIs)
	// ------------------------------------------------------------
	fmt.Println("\n===== RFC3339 FORMAT =====")

	rfc := t.Format(time.RFC3339)
	p("RFC3339:", rfc)

	// Parse RFC3339 string back to time
	t1, _ := time.Parse(time.RFC3339, "2012-11-01T22:08:41+00:00")
	p("Parsed RFC3339:", t1)

	// ------------------------------------------------------------
	// 3️. COMMON FORMAT PATTERNS
	// ------------------------------------------------------------
	fmt.Println("\n===== COMMON FORMATS =====")

	p("12-hour format:", t.Format("3:04PM"))
	p("24-hour format:", t.Format("15:04"))

	// Go’s reference layout format (VERY IMPORTANT)
	p("Full layout:",
		t.Format("Mon Jan _2 15:04:05 2006"))

	// High precision timestamp
	p("High precision:",
		t.Format("2006-01-02T15:04:05.999999-07:00"))

	// ------------------------------------------------------------
	// 4️. CUSTOM STRING PARSING
	// ------------------------------------------------------------
	fmt.Println("\n===== CUSTOM PARSING =====")

	form := "3 04 PM"

	parsed, _ := time.Parse(form, "8 41 PM")
	p("Parsed custom time:", parsed)

	// ------------------------------------------------------------
	// 5️. MANUAL FORMAT USING PRINTF
	// ------------------------------------------------------------
	fmt.Println("\n===== MANUAL FORMAT (Printf) =====")

	fmt.Printf("%d-%02d-%02dT%02d:%02d:%02d-00:00\n",
		t.Year(), t.Month(), t.Day(),
		t.Hour(), t.Minute(), t.Second())

	// ------------------------------------------------------------
	// 6️. PARSE ERROR HANDLING
	// ------------------------------------------------------------
	fmt.Println("\n===== PARSE ERROR =====")

	_, err := time.Parse("Mon Jan _2 15:04:05 2006", "8:41PM")

	if err != nil {
		fmt.Println("Error while parsing:", err)
	} else {
		fmt.Println("Parsed successfully")
	}

	// ------------------------------------------------------------
	// 7️. DIFFERENT FORMAT EXAMPLES (REAL WORLD)
	// ------------------------------------------------------------
	fmt.Println("\n===== REAL WORLD FORMATS =====")

	// API style
	fmt.Println("API Format:", t.Format(time.RFC3339Nano))

	// Database style
	fmt.Println("DB Format:", t.Format("2006-01-02 15:04:05"))

	// Log format
	fmt.Println("Log Format:", t.Format("2006/01/02 15:04:05"))

	// Human readable
	fmt.Println("Readable:", t.Format("Monday, 02 Jan 2006 03:04 PM"))

	// ------------------------------------------------------------
	// 8️. IMPORTANT RULE: GO TIME LAYOUT SYSTEM
	// ------------------------------------------------------------
	fmt.Println("\n===== GO LAYOUT RULE =====")

	fmt.Println("Reference time:")
	fmt.Println("Mon Jan 2 15:04:05 MST 2006")

	fmt.Println("This exact date is used to define formats!")

	// Example mapping:
	fmt.Println("2006 = year")
	fmt.Println("01   = month")
	fmt.Println("02   = day")
	fmt.Println("15   = hour (24h)")
	fmt.Println("03   = hour (12h)")
	fmt.Println("04   = minute")
	fmt.Println("05   = second")
}