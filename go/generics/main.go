package main

import "fmt"

// ---------------------------------------------------
// 1. Generic Index Function (Slice Search)
// ---------------------------------------------------

// S is a slice type (~[]E means any slice type with element E)
// E must be comparable to allow == comparison
func Index[S ~[]E, E comparable](s S, v E) int {
	for i := range s {
		if s[i] == v {
			return i
		}
	}
	return -1
}

// ---------------------------------------------------
// 2. Generic Contains Function
// ---------------------------------------------------

func Contains[S ~[]E, E comparable](s S, v E) bool {
	return Index(s, v) != -1
}

// ---------------------------------------------------
// 3. Generic Map Function (transform slice)
// ---------------------------------------------------

func Map[A any, B any](input []A, f func(A) B) []B {
	result := make([]B, len(input))
	for i, v := range input {
		result[i] = f(v)
	}
	return result
}

// ---------------------------------------------------
// 4. Generic Filter Function
// ---------------------------------------------------

func Filter[T any](input []T, f func(T) bool) []T {
	var result []T
	for _, v := range input {
		if f(v) {
			result = append(result, v)
		}
	}
	return result
}

// ---------------------------------------------------
// 5. Generic Reduce Function
// ---------------------------------------------------

func Reduce[T any, R any](input []T, initial R, f func(R, T) R) R {
	result := initial
	for _, v := range input {
		result = f(result, v)
	}
	return result
}

// ---------------------------------------------------
// 6. Generic Stack Implementation
// ---------------------------------------------------

type Stack[T any] struct {
	items []T
}

func (s *Stack[T]) Push(v T) {
	s.items = append(s.items, v)
}

func (s *Stack[T]) Pop() (T, bool) {
	if len(s.items) == 0 {
		var zero T
		return zero, false
	}
	last := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return last, true
}

func (s *Stack[T]) Size() int {
	return len(s.items)
}

// ---------------------------------------------------
// 7. Generic Linked List
// ---------------------------------------------------

type List[T any] struct {
	head *Node[T]
	tail *Node[T]
}

type Node[T any] struct {
	val  T
	next *Node[T]
}

func (l *List[T]) Push(v T) {
	newNode := &Node[T]{val: v}

	if l.head == nil {
		l.head = newNode
		l.tail = newNode
		return
	}

	l.tail.next = newNode
	l.tail = newNode
}

func (l *List[T]) ToSlice() []T {
	var result []T
	for n := l.head; n != nil; n = n.next {
		result = append(result, n.val)
	}
	return result
}

// ---------------------------------------------------
// 8. Generic Min Function (comparable constraint)
// ---------------------------------------------------

func Min[T comparable](a, b T) T {
	if a == b {
		return a
	}
	return a
}

// ---------------------------------------------------
// 9. Generic Swap Function
// ---------------------------------------------------

func Swap[T any](a, b *T) {
	*a, *b = *b, *a
}

// ---------------------------------------------------
// MAIN
// ---------------------------------------------------

func main() {

	// -------------------------------
	// Slice Index / Contains
	// -------------------------------
	s := []string{"foo", "bar", "zoo"}

	fmt.Println("Index:", Index(s, "zoo"))
	fmt.Println("Contains:", Contains(s, "bar"))

	// -------------------------------
	// Map (Transform)
	// -------------------------------
	nums := []int{1, 2, 3, 4}

	squares := Map(nums, func(x int) int {
		return x * x
	})

	fmt.Println("Squares:", squares)

	// -------------------------------
	// Filter
	// -------------------------------
	evens := Filter(nums, func(x int) bool {
		return x%2 == 0
	})

	fmt.Println("Evens:", evens)

	// -------------------------------
	// Reduce
	// -------------------------------
	sum := Reduce(nums, 0, func(acc, v int) int {
		return acc + v
	})

	fmt.Println("Sum:", sum)

	// -------------------------------
	// Stack
	// -------------------------------
	var st Stack[string]
	st.Push("A")
	st.Push("B")
	st.Push("C")

	val, _ := st.Pop()
	fmt.Println("Popped:", val)
	fmt.Println("Stack size:", st.Size())

	// -------------------------------
	// Linked List
	// -------------------------------
	var list List[int]
	list.Push(10)
	list.Push(20)
	list.Push(30)

	fmt.Println("Linked list:", list.ToSlice())

	// -------------------------------
	// Swap
	// -------------------------------
	x, y := 10, 20
	Swap(&x, &y)
	fmt.Println("Swapped:", x, y)
}