package main

import "fmt"

func main() {

	// ---------------------------------------------------
	// 1. Basic Closure (state preserved)
	// ---------------------------------------------------
	fmt.Println("Basic Closure Counter")
	nextInt := counter()

	fmt.Println(nextInt()) // 1
	fmt.Println(nextInt()) // 2
	fmt.Println(nextInt()) // 3

	// New instance → new memory/state
	newCounter := counter()
	fmt.Println(newCounter()) // 1

	// ---------------------------------------------------
	// 2. Multiple Independent Closures
	// ---------------------------------------------------
	fmt.Println("\nIndependent Counters")

	c1 := counter()
	c2 := counter()

	fmt.Println("c1:", c1()) // 1
	fmt.Println("c1:", c1()) // 2
	fmt.Println("c2:", c2()) // 1
	fmt.Println("c1:", c1()) // 3
	fmt.Println("c2:", c2()) // 2

	// ---------------------------------------------------
	// 3. Closure with Parameters (Factory pattern)
	// ---------------------------------------------------
	fmt.Println("\nMultiplier Closure")

	double := multiplier(2)
	triple := multiplier(3)

	fmt.Println("Double 5:", double(5))
	fmt.Println("Triple 5:", triple(5))

	// ---------------------------------------------------
	// 4. Closure as Generator
	// ---------------------------------------------------
	fmt.Println("\nFibonacci Generator")

	fib := fibonacciGenerator()
	for i := 0; i < 6; i++ {
		fmt.Println(fib())
	}

	// ---------------------------------------------------
	// 5. Closure modifying external variable
	// ---------------------------------------------------
	fmt.Println("\nClosure capturing external variable")

	x := 10
	addToX := func(v int) int {
		x += v
		return x
	}

	fmt.Println(addToX(5)) // 15
	fmt.Println(addToX(5)) // 20

	// ---------------------------------------------------
	// 6. Closure as function parameter
	// ---------------------------------------------------
	fmt.Println("\nUsing closure as callback")

	result := operate(5, 3, func(a, b int) int {
		return a * b
	})
	fmt.Println("Multiplication:", result)

	// ---------------------------------------------------
	// 7. Closure for configuration (Real world use case)
	// ---------------------------------------------------
	fmt.Println("\nLogger Closure")

	infoLogger := logger("INFO")
	errorLogger := logger("ERROR")

	infoLogger("Server started")
	errorLogger("Database failed")

	// ---------------------------------------------------
	// 8. Stateful accumulator
	// ---------------------------------------------------
	fmt.Println("\nAccumulator")

	acc := accumulator()
	fmt.Println(acc(10))
	fmt.Println(acc(20))
	fmt.Println(acc(30))
}

////////////////////////////////////////////////////////
// Closure Implementations
////////////////////////////////////////////////////////

// 1. Basic counter closure
func counter() func() int {
	i := 0 // captured variable
	return func() int {
		i++
		return i
	}
}

// 2. Closure factory with parameter
func multiplier(factor int) func(int) int {
	return func(x int) int {
		return x * factor
	}
}

// 3. Fibonacci generator using closure
func fibonacciGenerator() func() int {
	a, b := 0, 1
	return func() int {
		a, b = b, a+b
		return a
	}
}

// 4. Closure as parameter
func operate(a, b int, op func(int, int) int) int {
	return op(a, b)
}

// 5. Logger factory (real-world closure)
func logger(prefix string) func(string) {
	return func(message string) {
		fmt.Println(prefix + ":", message)
	}
}

// 6. Accumulator closure
func accumulator() func(int) int {
	total := 0
	return func(value int) int {
		total += value
		return total
	}
}