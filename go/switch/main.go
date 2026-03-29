package main

import (
	"fmt"
	"time"
)

func main() {

	// ----------------------------------------
	// 1) BASIC SWITCH (value comparison)
	// ----------------------------------------
	number := 3
	fmt.Print("Write ", number, " as ")

	// Switch checks the value of "number"
	switch number {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	case 3:
		fmt.Println("three")
	}

	// ----------------------------------------
	// 2) SWITCH WITH MULTIPLE VALUES IN ONE CASE
	// ----------------------------------------
	// Get today's weekday (Mon, Tue, etc.)
	switch time.Now().Weekday() {

	// Multiple values in one case using comma
	case time.Friday, time.Saturday:
		fmt.Println("It's the weekend vibe 😎")

	default:
		fmt.Println("It's a working day")
	}

	// ----------------------------------------
	// 3) SWITCH WITHOUT A CONDITION (acts like IF-ELSE)
	// ----------------------------------------
	// This switch has no value → behaves like if/else chain.
	currentTime := time.Now()

	switch {
	case currentTime.Hour() < 12:
		fmt.Println("Good morning ☀️")

	case currentTime.Hour() < 18:
		fmt.Println("Good afternoon 🌤")

	default:
		fmt.Println("Good evening 🌙")
	}

	// ----------------------------------------
	// 4) TYPE SWITCH (detect variable data type)
	// ----------------------------------------
	// This function checks the TYPE of any value passed to it.
	checkType := func(value interface{}) {

		// Type switch syntax: value.(type)
		switch v := value.(type) {

		case bool:
			fmt.Println("This is a boolean")

		case int:
			fmt.Println("This is an integer")

		case string:
			fmt.Println("This is a string")

		default:
			fmt.Printf("Unknown type: %T\n", v)
		}
	}

	// Calling the function with different types
	checkType(false)
	checkType(42)
	checkType("hello")
}
