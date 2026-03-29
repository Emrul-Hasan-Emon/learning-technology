package main

import (
	"fmt"
	"slices"
)

func main() {

	// ======================================================
	// 1) NIL SLICE (slice with no data yet)
	// ======================================================
	var names []string
	fmt.Println("Nil slice:", names)
	fmt.Println("Is nil?", names == nil)
	fmt.Println("Length:", len(names), "Capacity:", cap(names))

	// ======================================================
	// 2) CREATE SLICE USING make()
	// make(type, length, capacity optional)
	// ======================================================
	names = make([]string, 3)
	fmt.Println("Empty slice:", names, "len:", len(names), "cap:", cap(names))

	// Set values
	names[0] = "Go"
	names[1] = "Java"
	names[2] = "Python"
	fmt.Println("After set:", names)

	// Get value
	fmt.Println("Index 1:", names[1])

	// ======================================================
	// 3) APPEND VALUES (very common in Go)
	// ======================================================
	names = append(names, "Rust")
	names = append(names, "C++", "JavaScript")
	fmt.Println("After append:", names)

	fmt.Println("Length:", len(names), "Capacity:", cap(names))

	// ======================================================
	// 4) COPY SLICE (important: slices share memory!)
	// ======================================================
	clone := make([]string, len(names))
	copy(clone, names)
	fmt.Println("Cloned slice:", clone)

	// ======================================================
	// 5) SLICE OPERATIONS (sub-slicing)
	// ======================================================
	// [start : end]  → end NOT included
	part1 := names[1:4]
	fmt.Println("names[1:4]:", part1)

	part2 := names[:3]
	fmt.Println("names[:3]:", part2)

	part3 := names[3:]
	fmt.Println("names[3:]:", part3)

	// ======================================================
	// 6) DECLARE SLICE DIRECTLY
	// ======================================================
	letters := []string{"A", "B", "C"}
	fmt.Println("Declared slice:", letters)

	// ======================================================
	// 7) COMPARE SLICES (Go 1.21+ slices package)
	// ======================================================
	letters2 := []string{"A", "B", "C"}

	if slices.Equal(letters, letters2) {
		fmt.Println("letters == letters2")
	}

	// ======================================================
	// 8) REMOVE ELEMENT FROM SLICE
	// Remove index 2
	// ======================================================
	index := 2
	names = append(names[:index], names[index+1:]...)
	fmt.Println("After delete index 2:", names)

	// ======================================================
	// 9) INSERT ELEMENT INTO SLICE
	// Insert at index 1
	// ======================================================
	pos := 1
	value := "Swift"

	names = append(names[:pos], append([]string{value}, names[pos:]...)...)
	fmt.Println("After insert:", names)

	// ======================================================
	// 10) LOOP THROUGH SLICE
	// ======================================================
	fmt.Println("Looping slice:")
	for i, v := range names {
		fmt.Println(i, v)
	}

	// ======================================================
	// 11) MULTI-DIMENSIONAL SLICES (dynamic rows)
	// ======================================================
	matrix := make([][]int, 3)

	for i := range 3 {
		matrix[i] = make([]int, i+1)
		for j := range i + 1 {
			matrix[i][j] = i + j
		}
	}
	fmt.Println("2D Slice:", matrix)

	// ======================================================
	// 12) CLEAR SLICE
	// ======================================================
	names = names[:0]
	fmt.Println("Cleared slice:", names, "len:", len(names), "cap:", cap(names))
}
