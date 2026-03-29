package main

import "fmt"

func main() {

	// ----------------------------------------
	// 1) SIMPLE IF–ELSE
	// ----------------------------------------
	// 7 % 2 gives remainder after division by 2.
	// If remainder is 0 → number is EVEN
	// If remainder is 1 → number is ODD
	if 7%2 == 0 {
		fmt.Println("7 is even")
	} else {
		fmt.Println("7 is odd")
	}

	// ----------------------------------------
	// 2) IF WITHOUT ELSE
	// ----------------------------------------
	// This block runs only if the condition is true.
	// If false, it simply skips the block.
	if 8%4 == 0 {
		fmt.Println("8 is divisible by 4")
	}

	// ----------------------------------------
	// 3) USING LOGICAL OR (||)
	// ----------------------------------------
	// || means OR → at least one condition must be true.
	// Here we check if 8 OR 7 is even.
	if 8%2 == 0 || 7%2 == 0 {
		fmt.Println("either 8 or 7 are even")
	}

	// ----------------------------------------
	// 4) IF WITH SHORT VARIABLE DECLARATION
	// ----------------------------------------
	// You can declare a variable inside an if statement.
	// This variable exists ONLY inside this if-else block.
	if num := 9; num < 0 {
		fmt.Println(num, "is negative")
	} else if num < 10 {
		// This runs because 9 is not < 0 but is < 10
		fmt.Println(num, "has 1 digit")
	} else {
		fmt.Println(num, "has multiple digits")
	}
}
