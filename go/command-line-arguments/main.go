package main

import (
	"flag"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {

	fmt.Println("===== RAW ARGUMENTS =====")

	// 1️. All arguments including program name
	fmt.Println("os.Args:", os.Args)

	// 2️ Arguments excluding program name
	if len(os.Args) > 1 {
		fmt.Println("Args without program:", os.Args[1:])
	}

	// 3️. Access argument safely by index
	if len(os.Args) > 3 {
		fmt.Println("4th argument:", os.Args[3])
	} else {
		fmt.Println("4th argument not provided")
	}

	fmt.Println("\n===== SAFE ARGUMENT HANDLING =====")

	// 4️. Loop through arguments
	for i, arg := range os.Args {
		fmt.Printf("Arg %d = %s\n", i, arg)
	}

	// 5️. Check argument count
	fmt.Println("Argument count:", len(os.Args)-1)

	fmt.Println("\n===== SIMPLE CUSTOM PARSER =====")

	// 6️. Manual argument parsing example
	for _, arg := range os.Args[1:] {
		if arg == "hello" {
			fmt.Println("Hello detected 👋")
		}
		if arg == "bye" {
			fmt.Println("Bye detected 👋")
		}
	}

	fmt.Println("\n===== INTEGER ARGUMENT PARSING =====")

	// 7️. Convert argument to int safely
	if len(os.Args) > 1 {
		num, err := strconv.Atoi(os.Args[1])
		if err == nil {
			fmt.Println("Parsed integer:", num)
		} else {
			fmt.Println("Argument is not an integer")
		}
	}

	fmt.Println("\n===== SUM MULTIPLE NUMBERS FROM CLI =====")

	sum := 0
	for _, arg := range os.Args[1:] {
		n, err := strconv.Atoi(arg)
		if err == nil {
			sum += n
		}
	}
	fmt.Println("Sum of numeric args:", sum)

	fmt.Println("\n===== KEY=VALUE STYLE ARGUMENTS =====")

	// Example: ./app name=emon age=25 city=dhaka
	for _, arg := range os.Args[1:] {
		if strings.Contains(arg, "=") {
			parts := strings.SplitN(arg, "=", 2)
			fmt.Printf("Key: %s Value: %s\n", parts[0], parts[1])
		}
	}

	fmt.Println("\n===== FLAG PACKAGE (REAL CLI STYLE) =====")

	// 8️. Define flags
	name := flag.String("name", "Guest", "your name")
	age := flag.Int("age", 0, "your age")
	isAdmin := flag.Bool("admin", false, "admin user?")
	langs := flag.String("langs", "go,js", "comma separated languages")

	flag.Parse()

	fmt.Println("Flag name:", *name)
	fmt.Println("Flag age:", *age)
	fmt.Println("Flag admin:", *isAdmin)
	fmt.Println("Flag langs:", strings.Split(*langs, ","))

	fmt.Println("\nRemaining args after flags:", flag.Args())

	fmt.Println("\n===== SUBCOMMAND STYLE CLI =====")

	// 9️. Subcommand example
	if len(os.Args) > 1 {
		switch os.Args[1] {
		case "greet":
			fmt.Println("Subcommand: greet")
		case "version":
			fmt.Println("Version 1.0.0")
		case "help":
			fmt.Println("Available commands: greet, version, help")
		}
	}

	fmt.Println("\n===== ENV VARIABLES + CLI =====")

	// 10. Environment variables
	os.Setenv("APP_MODE", "development")
	fmt.Println("APP_MODE:", os.Getenv("APP_MODE"))

	fmt.Println("\n===== EXIT CODES =====")

	// 11. Exit with error code if no args
	if len(os.Args) == 1 {
		fmt.Println("No arguments provided!")
		os.Exit(1)
	}

	fmt.Println("\nProgram completed successfully!")
}

/**
go build main.go

./main 10 20 30
./main hello bye
./main name=emon age=25 city=dhaka
./main -name=Emon -age=25 -admin=true -langs=go,java,js extraArg
./main greet
*/