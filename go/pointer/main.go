package main

import "fmt"

func main() {

	// ---------------------------------------------------
	// 1. Basic Pointer
	// ---------------------------------------------------
	x := 10
	var p *int = &x // pointer storing address of x

	fmt.Println("Value of x:", x)
	fmt.Println("Address of x:", &x)
	fmt.Println("Pointer p holds:", p)
	fmt.Println("Value using pointer:", *p)

	// ---------------------------------------------------
	// 2. Modify value using pointer
	// ---------------------------------------------------
	*p = 20
	fmt.Println("\nAfter modifying via pointer:", x)

	// ---------------------------------------------------
	// 3. Pass by Value vs Pass by Pointer
	// ---------------------------------------------------
	i := 5
	fmt.Println("\nOriginal i:", i)

	changeByValue(i)
	fmt.Println("After changeByValue:", i)

	changeByPointer(&i)
	fmt.Println("After changeByPointer:", i)

	// ---------------------------------------------------
	// 4. Pointer with Struct (Very common in Go)
	// ---------------------------------------------------
	user := User{"John", 25}
	updateUser(&user)
	fmt.Println("\nUpdated struct:", user)

	// ---------------------------------------------------
	// 5. Pointer with Arrays
	// ---------------------------------------------------
	arr := [3]int{1, 2, 3}
	doubleArray(&arr)
	fmt.Println("\nArray after pointer function:", arr)

	// ---------------------------------------------------
	// 6. Nil Pointer
	// ---------------------------------------------------
	var ptr *int
	if ptr == nil {
		fmt.Println("\nPointer is nil (no memory assigned)")
	}

	// ---------------------------------------------------
	// 7. new() keyword
	// ---------------------------------------------------
	num := new(int) // allocates memory, default value 0
	fmt.Println("\nValue from new():", *num)

	*num = 50
	fmt.Println("After update:", *num)

	// ---------------------------------------------------
	// 8. Pointer to Pointer (double pointer)
	// ---------------------------------------------------
	a := 100
	p1 := &a
	p2 := &p1

	fmt.Println("\nValue using **p2:", **p2)

	// ---------------------------------------------------
	// 9. Slice vs Pointer (Important concept)
	// ---------------------------------------------------
	slice := []int{1, 2, 3}
	modifySlice(slice)
	fmt.Println("\nSlice modified without pointer:", slice)

	// ---------------------------------------------------
	// 10. Returning Pointer from Function
	// ---------------------------------------------------
	ptrNum := createNumber()
	fmt.Println("\nReturned pointer value:", *ptrNum)
}

////////////////////////////////////////////////////////
// Function Examples
////////////////////////////////////////////////////////

// Pass by value (copy)
func changeByValue(val int) {
	val = 0
}

// Pass by pointer (reference)
func changeByPointer(ptr *int) {
	*ptr = 0
}

// Struct example
type User struct {
	Name string
	Age  int
}

func updateUser(u *User) {
	u.Name = "Updated Name"
	u.Age = 99
}

// Pointer with array
func doubleArray(arr *[3]int) {
	for i := range arr {
		arr[i] *= 2
	}
}

// Slice behaves like reference (no pointer needed)
func modifySlice(s []int) {
	s[0] = 999
}

// Return pointer from function
func createNumber() *int {
	x := 42
	return &x // safe in Go (escape analysis)
}