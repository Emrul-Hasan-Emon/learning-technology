package main

import "fmt"

func main() {

	// ---------------------------------------------------
	// 1. Basic Recursion – Factorial
	// ---------------------------------------------------
	fmt.Println("Factorial(5):", factorial(5))

	// ---------------------------------------------------
	// 2. Recursive Anonymous Function (IMPORTANT)
	// ---------------------------------------------------
	var fib func(int) int

	fib = func(n int) int {
		if n < 2 {
			return n
		}
		return fib(n-1) + fib(n-2)
	}

	fmt.Println("Fibonacci(7):", fib(7))

	// ---------------------------------------------------
	// 3. Tail Recursion (Optimizable recursion style)
	// ---------------------------------------------------
	fmt.Println("Tail factorial(5):", tailFactorial(5, 1))

	// ---------------------------------------------------
	// 4. Recursion with Multiple Returns
	// ---------------------------------------------------
	sum, count := sumArray([]int{1, 2, 3, 4, 5}, 0)
	fmt.Println("Sum:", sum, "Count:", count)

	// ---------------------------------------------------
	// 5. Tree Recursion Example
	// ---------------------------------------------------
	root := &Node{
		Value: 1,
		Left: &Node{
			Value: 2,
			Left:  &Node{Value: 4},
			Right: &Node{Value: 5},
		},
		Right: &Node{
			Value: 3,
		},
	}

	fmt.Print("Tree Traversal (Inorder): ")
	inorder(root)
	fmt.Println()

	// ---------------------------------------------------
	// 6. Backtracking Recursion
	// ---------------------------------------------------
	fmt.Println("Subsets of [1,2,3]:")
	generateSubsets([]int{1, 2, 3}, []int{}, 0)

	// ---------------------------------------------------
	// 7. Recursive Closure Counter
	// ---------------------------------------------------
	counter := recursiveCounter()
	fmt.Println("Recursive counter:", counter())
	fmt.Println("Recursive counter:", counter())
	fmt.Println("Recursive counter:", counter())
}

////////////////////////////////////////////////////////
// 1. Basic Recursion
////////////////////////////////////////////////////////

func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

////////////////////////////////////////////////////////
// 2. Tail Recursion
////////////////////////////////////////////////////////

func tailFactorial(n, acc int) int {
	if n == 0 {
		return acc
	}
	return tailFactorial(n-1, n*acc)
}

////////////////////////////////////////////////////////
// 3. Recursion with Multiple Returns
////////////////////////////////////////////////////////

func sumArray(arr []int, index int) (int, int) {
	if index == len(arr) {
		return 0, 0
	}
	sum, count := sumArray(arr, index+1)
	return arr[index] + sum, count + 1
}

////////////////////////////////////////////////////////
// 4. Tree Recursion (Binary Tree Traversal)
////////////////////////////////////////////////////////

type Node struct {
	Value int
	Left  *Node
	Right *Node
}

func inorder(node *Node) {
	if node == nil {
		return
	}
	inorder(node.Left)
	fmt.Print(node.Value, " ")
	inorder(node.Right)
}

////////////////////////////////////////////////////////
// 5. Backtracking Recursion (Subsets)
////////////////////////////////////////////////////////

func generateSubsets(nums []int, current []int, index int) {
	if index == len(nums) {
		fmt.Println(current)
		return
	}

	// include element
	generateSubsets(nums, append(current, nums[index]), index+1)

	// exclude element
	generateSubsets(nums, current, index+1)
}

////////////////////////////////////////////////////////
// 6. Recursive Closure (advanced)
////////////////////////////////////////////////////////

func recursiveCounter() func() int {
	count := 0

	var fn func() int
	fn = func() int {
		count++
		return count
	}

	return fn
}