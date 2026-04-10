package main

import (
	"fmt"
	"math"
)

// 1. Interface Definition

// geometry is an interface.
// Any type that implements BOTH area() and perim()
// automatically satisfies this interface.
type geometry interface {
	area() float64
	perim() float64
}

// 2. Struct Types

// rect type
type rect struct {
	width, height float64
}

// circle type
type circle struct {
	radius float64
}

// 3. Implementing Interface Methods for rect

// rect implements geometry because it has area() and perim()

func (r rect) area() float64 {
	return r.width * r.height
}

func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

// 4. Implementing Interface Methods for circle

// circle ALSO implements geometry automatically

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

// 5. Function that accepts Interface

// measure can accept ANY type that satisfies geometry
func measure(g geometry) {
	fmt.Println("Shape:", g)       // prints actual struct
	fmt.Println("Area:", g.area()) // dynamic dispatch
	fmt.Println("Perim:", g.perim())
}

// 6. Type Assertion (Checking underlying type)

// Detect if the geometry is specifically a circle
func detectCircle(g geometry) {

	// type assertion
	c, ok := g.(circle)

	if ok {
		fmt.Println("This is a circle with radius:", c.radius)
	} else {
		fmt.Println("This is NOT a circle")
	}
}

// 7. Main Function

func main() {

	// create concrete types
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	// Both rect and circle can be used as geometry
	measure(r)
	measure(c)

	// Type assertion demo
	detectCircle(r)
	detectCircle(c)
}