package main

import "fmt"

func main() {

	// ======================================================
	// 1) DECLARING AN EMPTY ARRAY (default values = 0)
	// ======================================================
	var numbers [5]int
	fmt.Println("Empty array:", numbers)

	// Set values using index
	numbers[0] = 10
	numbers[1] = 20
	numbers[4] = 50
	fmt.Println("After setting values:", numbers)

	// Get value from index
	fmt.Println("Value at index 1:", numbers[1])

	// Length of array
	fmt.Println("Length:", len(numbers))

	// ======================================================
	// 2) DECLARE & INITIALIZE ARRAY IN ONE LINE
	// ======================================================
	scores := [5]int{90, 85, 70, 95, 88}
	fmt.Println("Scores:", scores)

	// Go can auto-count array size using ...
	fruits := [...]string{"Apple", "Banana", "Mango"}
	fmt.Println("Fruits:", fruits)

	// ======================================================
	// 3) SET VALUE AT SPECIFIC INDEX DURING DECLARATION
	// ======================================================
	// Index 2 = 100, Index 4 = 500 (others default 0)
	special := [...]int{2: 100, 4: 500}
	fmt.Println("Special array:", special)

	// ======================================================
	// 4) LOOP THROUGH ARRAY (classic for loop)
	// ======================================================
	fmt.Println("Loop using for:")
	for i := 0; i < len(scores); i++ {
		fmt.Println("Index:", i, "Value:", scores[i])
	}

	// ======================================================
	// 5) LOOP USING RANGE (most common in Go)
	// ======================================================
	fmt.Println("Loop using range:")

	for index, value := range scores {
		fmt.Println(index, value)
	}

	// If you only need values
	fmt.Println("Only values:")
	for _, value := range scores {
		fmt.Println(value)
	}

	// ======================================================
	// 6) COPY ARRAY (arrays are value types in Go)
	// ======================================================
	original := [3]int{1, 2, 3}
	copyArr := original // creates a FULL COPY

	copyArr[0] = 999

	fmt.Println("Original:", original)
	fmt.Println("Copied:", copyArr)

	// ======================================================
	// 7) COMPARE ARRAYS
	// ======================================================
	a := [3]int{1, 2, 3}
	b := [3]int{1, 2, 3}
	c := [3]int{3, 2, 1}

	fmt.Println("a == b ?", a == b) // true
	fmt.Println("a == c ?", a == c) // false

	// ======================================================
	// 8) MULTI-DIMENSIONAL ARRAY (2D ARRAY)
	// ======================================================
	var matrix [2][3]int

	// Fill using loops
	for i := range 2 {
		for j := range 3 {
			matrix[i][j] = i + j
		}
	}

	fmt.Println("Matrix using loops:", matrix)

	// Initialize directly
	matrix = [2][3]int{
		{1, 2, 3},
		{4, 5, 6},
	}
	fmt.Println("Matrix direct init:", matrix)

	// ======================================================
	// 9) SUM ALL ELEMENTS OF ARRAY
	// ======================================================
	sum := 0
	for _, v := range scores {
		sum += v
	}
	fmt.Println("Sum of scores:", sum)

	// ======================================================
	// 10) FIND MAX VALUE IN ARRAY
	// ======================================================
	max := scores[0]
	for _, v := range scores {
		if v > max {
			max = v
		}
	}
	fmt.Println("Max score:", max)

}
