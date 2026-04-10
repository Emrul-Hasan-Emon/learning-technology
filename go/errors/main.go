package main

import (
	"errors"
	"fmt"
)

// 1. Function returning basic error

// f demonstrates standard Go error handling pattern
func f(arg int) (int, error) {

	// custom error condition
	if arg == 42 {
		return -1, errors.New("can't work with 42")
	}

	// success case: return result + nil error
	return arg + 3, nil
}

// 2. Sentinel Errors (predefined errors)

// Sentinel errors are reusable global error variables
var ErrOutOfTea = errors.New("no more tea available")
var ErrPower = errors.New("can't boil water")

// 3. Error Wrapping (VERY IMPORTANT)

// makeTea returns different error types
func makeTea(arg int) error {

	if arg == 2 {
		// direct sentinel error
		return ErrOutOfTea

	} else if arg == 4 {
		// wrapped error (adds context)
		// %w preserves original error for later inspection
		return fmt.Errorf("making tea: %w", ErrPower)
	}

	// no error
	return nil
}

// 4. MAIN FUNCTION

func main() {

	// ---------------------------------------------------
	// 1. Basic error handling pattern
	// ---------------------------------------------------

	for _, i := range []int{7, 42} {

		r, e := f(i)

		// always check error first
		if e != nil {
			fmt.Println("f failed:", e)
		} else {
			fmt.Println("f worked:", r)
		}
	}

	// ---------------------------------------------------
	// 2. Error handling with loops (range over integers)
	// ---------------------------------------------------

	for i := range 5 {

		err := makeTea(i)

		if err != nil {

			// ---------------------------------------------------
			// 3. error matching using errors.Is()
			// ---------------------------------------------------

			if errors.Is(err, ErrOutOfTea) {
				fmt.Println("We should buy new tea!")

			} else if errors.Is(err, ErrPower) {
				fmt.Println("Now it is dark!")

			} else {
				fmt.Printf("unknown error: %s\n", err)
			}

			continue
		}

		fmt.Println("Tea is ready!")
	}
}