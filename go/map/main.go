package main

import (
	"fmt"
	"maps" 
	"slices"
)

func main() {

	// ---------------------------------------------------
	// 1. Creating Maps
	// ---------------------------------------------------

	// Method 1: Using make()
	ages := make(map[string]int)

	// Method 2: Map literal (initialize with values)
	scores := map[string]int{
		"Alice": 90,
		"Bob":   85,
	}

	fmt.Println("Initial scores:", scores)

	// ---------------------------------------------------
	// 2. Add / Update values
	// ---------------------------------------------------

	ages["John"] = 25
	ages["Emma"] = 30
	ages["John"] = 26 // Update existing key

	fmt.Println("Ages:", ages)

	// ---------------------------------------------------
	// 3. Access value by key
	// ---------------------------------------------------

	age := ages["John"]
	fmt.Println("John age:", age)

	// ⚠️ Accessing non-existing key returns ZERO VALUE
	unknown := ages["Unknown"]
	fmt.Println("Unknown age (zero value):", unknown)

	// ---------------------------------------------------
	// 4. Check if key exists
	// ---------------------------------------------------

	value, exists := ages["Emma"]
	fmt.Println("Emma exists?", exists, "value:", value)

	value, exists = ages["NoOne"]
	fmt.Println("NoOne exists?", exists, "value:", value)

	// ---------------------------------------------------
	// 5. Length of map
	// ---------------------------------------------------
	fmt.Println("Total people:", len(ages))

	// ---------------------------------------------------
	// 6. Delete key
	// ---------------------------------------------------
	delete(ages, "Emma")
	fmt.Println("After deleting Emma:", ages)

	// delete on non-existing key is SAFE (no error)
	delete(ages, "Ghost")

	// ---------------------------------------------------
	// 7. Iterate over map (range loop)
	// ---------------------------------------------------

	fmt.Println("\nIterating map:")
	for key, value := range scores {
		fmt.Println(key, "=>", value)
	}

	// Only keys
	fmt.Println("\nOnly keys:")
	for key := range scores {
		fmt.Println(key)
	}

	// Only values
	fmt.Println("\nOnly values:")
	for _, value := range scores {
		fmt.Println(value)
	}

	// ---------------------------------------------------
	// 8. Clear entire map
	// ---------------------------------------------------
	clear(ages)
	fmt.Println("After clear:", ages)

	// ---------------------------------------------------
	// 9. Compare maps (Go 1.21+)
	// ---------------------------------------------------

	m1 := map[string]int{"a": 1, "b": 2}
	m2 := map[string]int{"a": 1, "b": 2}
	m3 := map[string]int{"a": 1, "b": 3}

	fmt.Println("m1 == m2 ?", maps.Equal(m1, m2))
	fmt.Println("m1 == m3 ?", maps.Equal(m1, m3))

	// ---------------------------------------------------
	// 10. Copy map
	// ---------------------------------------------------

	dst := make(map[string]int)
	maps.Copy(dst, m1)
	fmt.Println("Copied map:", dst)

	// ---------------------------------------------------
	// 11. Get all keys or values
	// ---------------------------------------------------

	keys := maps.Keys(m1)
	values := maps.Values(m1)

	fmt.Println("Keys:", keys)
	fmt.Println("Values:", values)

	// ---------------------------------------------------
	// 12. Sort keys (maps are UNORDERED!)
	// ---------------------------------------------------

	sortedKeys := maps.Keys(scores)
	slices.Sort(sortedKeys)

	fmt.Println("\nSorted iteration:")
	for _, k := range sortedKeys {
		fmt.Println(k, "=>", scores[k])
	}

	// ---------------------------------------------------
	// 13. Map as set (very common pattern)
	// ---------------------------------------------------

	set := make(map[string]bool)

	set["apple"] = true
	set["banana"] = true

	fmt.Println("\nIs apple in set?", set["apple"])
	fmt.Println("Is mango in set?", set["mango"]) // false

	// ---------------------------------------------------
	// 14. Map of slices
	// ---------------------------------------------------

	class := make(map[string][]string)

	class["Math"] = []string{"John", "Emma"}
	class["Science"] = append(class["Science"], "Alice")

	fmt.Println("\nMap of slices:", class)

	// ---------------------------------------------------
	// 15. Nested map
	// ---------------------------------------------------

	users := map[string]map[string]string{
		"user1": {
			"name": "John",
			"city": "Dhaka",
		},
	}

	fmt.Println("\nNested map:", users["user1"]["name"])

	// ---------------------------------------------------
	// 16. Passing map to function (maps are reference type)
	// ---------------------------------------------------

	updateMap(scores)
	fmt.Println("\nAfter function update:", scores)
}

// Maps are reference types → changes affect original map
func updateMap(m map[string]int) {
	m["Alice"] = 100
}