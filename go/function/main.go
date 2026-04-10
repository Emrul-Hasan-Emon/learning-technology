package main

import (
	"fmt"
	"errors"
)

func main() {

	// ---------------------------------------------------
	// 1. Basic Function
	// ---------------------------------------------------
	fmt.Println("Basic function:", add(2, 3))

	// ---------------------------------------------------
	// 2. Multiple Parameters (same type shorthand)
	// ---------------------------------------------------
	fmt.Println("Multiply:", multiply(3, 4))

	// ---------------------------------------------------
	// 3. Multiple Return Values (VERY IMPORTANT)
	// ---------------------------------------------------
	sum, product := sumAndProduct(3, 5)
	fmt.Println("Sum:", sum, "Product:", product)

	// ---------------------------------------------------
	// 4. Named Return Values
	// ---------------------------------------------------
	s, p := namedReturn(4, 6)
	fmt.Println("Named return -> Sum:", s, "Product:", p)

	// ---------------------------------------------------
	// 5. Ignore Return Value using _
	// ---------------------------------------------------
	sumOnly, _ := sumAndProduct(10, 20)
	fmt.Println("Ignore product:", sumOnly)

	// ---------------------------------------------------
	// 6. Function returning error (VERY COMMON)
	// ---------------------------------------------------
	result, err := divide(10, 2)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Division:", result)
	}

	// ---------------------------------------------------
	// 7. Variadic Function (... arguments)
	// ---------------------------------------------------
	fmt.Println("Variadic sum:", sumAll(1, 2, 3, 4, 5))

	// ---------------------------------------------------
	// 8. Anonymous Function (function without name)
	// ---------------------------------------------------
	func() {
		fmt.Println("I am anonymous function")
	}()

	// Anonymous function with parameters
	res := func(a int, b int) int {
		return a * b
	}(3, 5)
	fmt.Println("Anonymous result:", res)

	// ---------------------------------------------------
	// 9. Function as Value (Function Variable)
	// ---------------------------------------------------
	var operation func(int, int) int
	operation = add
	fmt.Println("Function variable:", operation(5, 6))

	// ---------------------------------------------------
	// 10. Function as Parameter (Callback)
	// ---------------------------------------------------
	result = calculate(4, 5, add)
	fmt.Println("Callback add:", result)

	result = calculate(4, 5, multiply)
	fmt.Println("Callback multiply:", result)

	// ---------------------------------------------------
	// 11. Function returning another function (Closure Factory)
	// ---------------------------------------------------
	double := multiplier(2)
	triple := multiplier(3)

	fmt.Println("Double 5:", double(5))
	fmt.Println("Triple 5:", triple(5))

	// ---------------------------------------------------
	// 12. Closure (captures outer variable)
	// ---------------------------------------------------
	counter := incrementer()
	fmt.Println("Counter:", counter())
	fmt.Println("Counter:", counter())
	fmt.Println("Counter:", counter())

	// ---------------------------------------------------
	// 13. Recursion
	// ---------------------------------------------------
	fmt.Println("Factorial 5:", factorial(5))

	// ---------------------------------------------------
	// 14. Defer Function
	// ---------------------------------------------------
	deferExample()

	// ---------------------------------------------------
	// 15. Panic & Recover
	// ---------------------------------------------------
	safeCall()
}

////////////////////////////////////////////////////////
// Function Definitions
////////////////////////////////////////////////////////

// 1. Basic function
func add(a int, b int) int {
	return a + b
}

// 2. Shorthand parameters (same type)
func multiply(a, b int) int {
	return a * b
}

// 3. Multiple return values
func sumAndProduct(a, b int) (int, int) {
	return a + b, a * b
}

// 4. Named return values
func namedReturn(a, b int) (sum int, product int) {
	sum = a + b
	product = a * b
	return // implicit return
}

// 5. Function returning error
func divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("cannot divide by zero")
	}
	return a / b, nil
}

// 6. Variadic function
func sumAll(nums ...int) int {
	total := 0
	for _, n := range nums {
		total += n
	}
	return total
}

// 7. Function as parameter (callback)
func calculate(a, b int, op func(int, int) int) int {
	return op(a, b)
}

// 8. Function returning function
func multiplier(factor int) func(int) int {
	return func(x int) int {
		return x * factor
	}
}

// 9. Closure example
func incrementer() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

// 10. Recursion
func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

// 11. Defer example
func deferExample() {
	fmt.Println("\nDefer Example Start")
	defer fmt.Println("This runs LAST")
	defer fmt.Println("This runs second")
	fmt.Println("This runs first")
}

// 12. Panic & Recover
func safeCall() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered from panic:", r)
		}
	}()

	panic("Something went wrong!")
}