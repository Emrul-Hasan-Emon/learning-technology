package main

import "fmt"

func main() {

	// ----------------------------------------
	// 1) WHILE-STYLE LOOP (Go doesn't have while keyword)
	// ----------------------------------------
	// This loop works like a "while" loop.
	// Start with i = 1 and keep looping while i <= 3
	i := 1
	for i <= 3 {
		fmt.Println(i) // print current value of i
		i = i + 1      // increase i by 1 each iteration
	}
	// Output: 1 2 3

	// ----------------------------------------
	// 2) CLASSIC FOR LOOP (like C/Java)
	// ----------------------------------------
	// Syntax: for initialization; condition; update
	for j := 0; j < 3; j++ {
		fmt.Println(j)
	}
	// Output: 0 1 2

	// ----------------------------------------
	// 3) RANGE LOOP OVER A NUMBER
	// ----------------------------------------
	// "range 3" generates numbers from 0 → 2
	// (total 3 iterations)
	for i := range 3 {
		fmt.Println("range", i)
	}
	// Output:
	// range 0
	// range 1
	// range 2

	// ----------------------------------------
	// 4) INFINITE LOOP
	// ----------------------------------------
	// "for { }" creates a loop that runs forever.
	// We stop it manually using break.
	for {
		fmt.Println("loop")
		break // exit the loop immediately
	}
	// Output: loop

	// ----------------------------------------
	// 5) RANGE + CONTINUE EXAMPLE
	// ----------------------------------------
	// Loop from 0 → 5 (6 iterations)
	for n := range 6 {

		// If number is even, skip this iteration
		if n%2 == 0 {
			continue
		}

		// Only odd numbers reach here
		fmt.Println(n)
	}
	// Output: 1 3 5
}
