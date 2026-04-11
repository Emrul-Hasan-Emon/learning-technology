package main

import (
	"cmp"
	"fmt"
	"slices"
)

type Person struct {
	name string
	age  int
}

func main() {

	// 1️. BASIC SORT (STRING)
	fmt.Println("===== BASIC STRING SORT =====")

	strs := []string{"c", "a", "b"}
	slices.Sort(strs)
	fmt.Println("Sorted strings:", strs)

	// 2️. BASIC SORT (INT)
	fmt.Println("\n===== BASIC INT SORT =====")

	ints := []int{7, 2, 4}
	slices.Sort(ints)
	fmt.Println("Sorted ints:", ints)

	// check if sorted
	fmt.Println("Is sorted?", slices.IsSorted(ints))

	// 3️. REVERSE SORT (using slices.Reverse)
	fmt.Println("\n===== REVERSE SORT =====")

	slices.Reverse(ints)
	fmt.Println("Reversed ints:", ints)

	// 4️. CUSTOM SORT (SortFunc) - STRING LENGTH
	fmt.Println("\n===== SORT BY STRING LENGTH =====")

	fruits := []string{"peach", "banana", "kiwi"}

	slices.SortFunc(fruits, func(a, b string) int {
		// compare by length
		return cmp.Compare(len(a), len(b))
	})

	fmt.Println("Sorted by length:", fruits)

	// 5️. SORT STRUCTS BY FIELD (AGE)
	fmt.Println("\n===== SORT STRUCTS BY AGE =====")

	people := []Person{
		{name: "Jax", age: 37},
		{name: "TJ", age: 25},
		{name: "Alex", age: 72},
		{name: "Bob", age: 25},
	}

	slices.SortFunc(people, func(a, b Person) int {
		return cmp.Compare(a.age, b.age)
	})

	fmt.Println("Sorted by age:", people)

	// 6️. MULTI-LEVEL SORT (AGE → NAME)
	fmt.Println("\n===== MULTI-LEVEL SORT (AGE THEN NAME) =====")

	slices.SortFunc(people, func(a, b Person) int {

		// first compare age
		if a.age != b.age {
			return cmp.Compare(a.age, b.age)
		}

		// if age same, compare name
		return cmp.Compare(a.name, b.name)
	})

	fmt.Println("Sorted by age then name:", people)

	// 7️. PARTIAL SORT (slice sub-range)
	fmt.Println("\n===== PARTIAL SORT =====")

	nums := []int{9, 1, 8, 3, 7, 2, 6}

	// sort only first 4 elements
	slices.Sort(nums[:4])

	fmt.Println("Partially sorted:", nums)

	// 8️. CHECK SORTED STRUCT LIST
	fmt.Println("\n===== CHECK SORTED STRUCT LIST =====")

	isSortedByAge := slices.IsSortedFunc(people, func(a, b Person) int {
		return cmp.Compare(a.age, b.age)
	})

	fmt.Println("Is sorted by age?", isSortedByAge)

	// 9️. DESCENDING ORDER SORT
	fmt.Println("\n===== DESCENDING SORT =====")

	slices.SortFunc(nums, func(a, b int) int {
		return cmp.Compare(b, a) // reverse order
	})

	fmt.Println("Descending:", nums)
}