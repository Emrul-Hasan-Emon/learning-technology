package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {

	// 1️. DEFER BASIC USAGE (cleanup is always executed)
	fmt.Println("===== DEFER + FILE HANDLING =====")

	path := filepath.Join(os.TempDir(), "defer.txt")

	f := createFile(path)

	// defer ensures file is always closed (even if panic happens)
	defer closeFile(f)

	writeFile(f)

	// 2️. SAFE RECOVERY WRAPPER (like middleware / interceptor)
	fmt.Println("\n===== RECOVER FROM PANIC =====")

	func() {

		// recover must be inside deferred function
		defer func() {
			if r := recover(); r != nil {
				fmt.Println("Recovered from panic:", r)
			}
		}()

		fmt.Println("about to panic...")

		mayPanic()

		// this line will NOT execute
		fmt.Println("this will not print")
	}()

	fmt.Println("program continues after recovery")

	// 3️. MULTIPLE PANIC SCENARIOS
	fmt.Println("\n===== MULTIPLE PANIC CASES =====")

	safeExecute("case-1", func() {
		panic("database connection failed")
	})

	safeExecute("case-2", func() {
		panic("nil pointer dereference")
	})

	safeExecute("case-3", func() {
		fmt.Println("no panic here")
	})

	// 4️. REAL-WORLD FLOW SIMULATION
	fmt.Println("\n===== REAL WORLD FLOW =====")

	func() {

		defer func() {
			if r := recover(); r != nil {
				fmt.Println("server recovered from crash:", r)
			}
		}()

		fmt.Println("server starting...")

		// simulate crash
		panic("server unexpected failure")

		// never executed
	}()

	fmt.Println("server still running (graceful recovery)")
}

// ------------------------------------------------------------
// FILE HANDLING FUNCTIONS (DEFER EXAMPLE)
// ------------------------------------------------------------

func createFile(p string) *os.File {
	fmt.Println("creating file")

	f, err := os.Create(p)
	if err != nil {
		panic(err)
	}
	return f
}

func writeFile(f *os.File) {
	fmt.Println("writing file")
	fmt.Fprintln(f, "hello world")
}

func closeFile(f *os.File) {
	fmt.Println("closing file")

	err := f.Close()
	if err != nil {
		panic(err)
	}
}

// ------------------------------------------------------------
// PANIC TRIGGER FUNCTION
// ------------------------------------------------------------

func mayPanic() {
	panic("a problem occurred")
}

// ------------------------------------------------------------
// SAFE EXECUTION WRAPPER (REAL PATTERN)
// ------------------------------------------------------------

func safeExecute(name string, fn func()) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in", name, ":", r)
		}
	}()

	fmt.Println("running:", name)
	fn()
	fmt.Println("finished:", name)
}