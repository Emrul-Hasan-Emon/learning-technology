package main

import (
	"fmt"
	"iter"
	"slices"
	"strings"
)

// Generic Linked List

type List[T any] struct {
	head, tail *element[T]
}

type element[T any] struct {
	next *element[T]
	val  T
}

// Push adds element to linked list

func (lst *List[T]) Push(v T) {
	if lst.tail == nil {
		lst.head = &element[T]{val: v}
		lst.tail = lst.head
	} else {
		lst.tail.next = &element[T]{val: v}
		lst.tail = lst.tail.next
	}
}

// Iterator: List → iter.Seq[T]

// All returns an ITERATOR over the linked list.
// iter.Seq[T] = function that yields values lazily.
func (lst *List[T]) All() iter.Seq[T] {
	return func(yield func(T) bool) {

		// traverse linked list node by node
		for e := lst.head; e != nil; e = e.next {

			// yield value to caller
			// if caller returns false → stop iteration
			if !yield(e.val) {
				return
			}
		}
	}
}

// Infinite Fibonacci Generator (Iterator)

// genFib returns an infinite sequence of Fibonacci numbers
func genFib() iter.Seq[int] {
	return func(yield func(int) bool) {

		a, b := 0, 1

		for {
			// send current value
			if !yield(a) {
				return
			}

			// update state
			a, b = b, a+b
		}
	}
}

// MAIN

func main() {

	// ---------------------------------------------------
	// 1. Linked List Iteration using range over iterator
	// ---------------------------------------------------

	lst := List[int]{}
	lst.Push(10)
	lst.Push(13)
	lst.Push(23)

	// range over custom iterator (lazy evaluation)
	for e := range lst.All() {
		fmt.Println("list element:", e)
	}

	// ---------------------------------------------------
	// 2. Collect iterator into slice
	// ---------------------------------------------------

	all := slices.Collect(lst.All())
	fmt.Println("collected slice:", all)

	// ---------------------------------------------------
	// 3. Built-in iterator: strings.SplitSeq
	// ---------------------------------------------------

	// SplitSeq returns an iterator instead of slice
	for part := range strings.SplitSeq("go-by-example", "-") {
		fmt.Println("part:", part)
	}

	// ---------------------------------------------------
	// 4. Infinite iterator (Fibonacci)
	// ---------------------------------------------------

	for n := range genFib() {

		// manual stop condition (VERY IMPORTANT)
		if n >= 10 {
			break
		}

		fmt.Println("fib:", n)
	}
}