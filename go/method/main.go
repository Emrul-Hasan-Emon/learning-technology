package main

import "fmt"

func main() {

	// ---------------------------------------------------
	// 1. Basic Struct
	// ---------------------------------------------------
	r := Rect{width: 10, height: 5}

	fmt.Println("Area:", r.area())
	fmt.Println("Perimeter:", r.perimeter())

	// ---------------------------------------------------
	// 2. Pointer vs Value Call (Go auto-handles)
	// ---------------------------------------------------
	rp := &r

	fmt.Println("\nCalling methods via pointer")
	fmt.Println("Area:", rp.area())       // pointer method
	fmt.Println("Perimeter:", rp.perimeter()) // value method

	// ---------------------------------------------------
	// 3. Method that modifies struct
	// ---------------------------------------------------
	r.scale(2)
	fmt.Println("\nAfter scaling:", r)

	// ---------------------------------------------------
	// 4. Methods on different structs
	// ---------------------------------------------------
	c := Circle{radius: 7}
	fmt.Println("\nCircle area:", c.area())

	// ---------------------------------------------------
	// 5. Method vs Function difference
	// ---------------------------------------------------
	fmt.Println("\nFunction area:", rectArea(r))

	// ---------------------------------------------------
	// 6. Method chaining
	// ---------------------------------------------------
	r.increment().increment()
	fmt.Println("\nAfter chaining:", r)

	// ---------------------------------------------------
	// 7. Getter & Setter pattern
	// ---------------------------------------------------
	r.setWidth(100)
	fmt.Println("\nGetter width:", r.getWidth())
}

// Struct Definitions

type Rect struct {
	width, height int
}

type Circle struct {
	radius int
}

// 1. Value Receiver Method (read-only)

func (r Rect) perimeter() int {
	return 2*r.width + 2*r.height
}

// 2. Pointer Receiver Method (modify struct)

func (r *Rect) area() int {
	return r.width * r.height
}

func (r *Rect) scale(factor int) {
	r.width *= factor
	r.height *= factor
}

// 3. Methods on another struct

func (c Circle) area() int {
	return 3 * c.radius * c.radius // simplified π≈3
}

// 4. Normal Function (not a method)

func rectArea(r Rect) int {
	return r.width * r.height
}

// 5. Method Chaining

func (r *Rect) increment() *Rect {
	r.width++
	r.height++
	return r
}

// 6. Getter & Setter Pattern

func (r Rect) getWidth() int {
	return r.width
}

func (r *Rect) setWidth(w int) {
	r.width = w
}