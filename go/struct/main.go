package main

import "fmt"

func main() {

	// ---------------------------------------------------
	// 1. Basic Struct Creation
	// ---------------------------------------------------
	p1 := Person{"Bob", 20}
	fmt.Println("Positional:", p1)

	// ---------------------------------------------------
	// 2. Named Fields Initialization (Recommended)
	// ---------------------------------------------------
	p2 := Person{name: "Alice", age: 30}
	fmt.Println("Named:", p2)

	// ---------------------------------------------------
	// 3. Partial Initialization (Zero values)
	// ---------------------------------------------------
	p3 := Person{name: "Fred"}
	fmt.Println("Zero values:", p3)

	// ---------------------------------------------------
	// 4. Pointer to Struct
	// ---------------------------------------------------
	p4 := &Person{name: "Ann", age: 40}
	fmt.Println("Pointer struct:", p4)

	// ---------------------------------------------------
	// 5. Constructor Function
	// ---------------------------------------------------
	p5 := NewPerson("Jon")
	fmt.Println("Constructor:", p5)

	// ---------------------------------------------------
	// 6. Access Struct Fields
	// ---------------------------------------------------
	s := Person{name: "Sean", age: 50}
	fmt.Println("Access field:", s.name)

	// ---------------------------------------------------
	// 7. Pointer automatically dereferenced
	// ---------------------------------------------------
	sp := &s
	fmt.Println("Access via pointer:", sp.age)

	sp.age = 51 // auto dereference
	fmt.Println("Modified via pointer:", s.age)

	// ---------------------------------------------------
	// 8. Anonymous Struct (one-time use)
	// ---------------------------------------------------
	dog := struct {
		name   string
		isGood bool
	}{
		name:   "Rex",
		isGood: true,
	}
	fmt.Println("Anonymous struct:", dog)

	// ---------------------------------------------------
	// 9. Struct with Methods
	// ---------------------------------------------------
	fmt.Println("\nMethod call:", s.greet())

	s.haveBirthday()
	fmt.Println("After birthday:", s.age)

	// ---------------------------------------------------
	// 10. Embedded Struct (Composition)
	// ---------------------------------------------------
	e := Employee{
		Person: Person{name: "Mike", age: 28},
		id:     101,
	}
	fmt.Println("\nEmbedded struct:", e)
	fmt.Println("Promoted field:", e.name)

	// ---------------------------------------------------
	// 11. Struct Comparison
	// ---------------------------------------------------
	a := Person{"John", 25}
	b := Person{"John", 25}
	fmt.Println("\nStruct equal?", a == b)

	// ---------------------------------------------------
	// 12. Slice of Structs
	// ---------------------------------------------------
	people := []Person{
		{"A", 10},
		{"B", 20},
		{"C", 30},
	}
	fmt.Println("\nSlice of structs:", people)
}

////////////////////////////////////////////////////////
// Struct Definition
////////////////////////////////////////////////////////

type Person struct {
	name string
	age  int
}

////////////////////////////////////////////////////////
// Constructor Function (Factory Pattern)
////////////////////////////////////////////////////////

func NewPerson(name string) *Person {
	p := Person{name: name}
	p.age = 42
	return &p
}

////////////////////////////////////////////////////////
// Methods on Struct
////////////////////////////////////////////////////////

// Value receiver (does not modify original)
func (p Person) greet() string {
	return "Hello, my name is " + p.name
}

// Pointer receiver (can modify original)
func (p *Person) haveBirthday() {
	p.age++
}

////////////////////////////////////////////////////////
// Embedded Struct (Composition over inheritance)
////////////////////////////////////////////////////////

type Employee struct {
	Person // embedded struct
	id     int
}