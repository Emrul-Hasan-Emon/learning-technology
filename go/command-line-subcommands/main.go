package main

import (
	"flag"
	"fmt"
	"os"
	"strings"
)

func main() {

	// 1. GLOBAL FLAGS (before subcommand)
	verbose := flag.Bool("v", false, "verbose mode")
	version := flag.Bool("version", false, "print version")

	flag.Parse()

	// Version flag works without subcommand
	if *version {
		fmt.Println("CLI Tool v1.0.0")
		return
	}

	// Must have subcommand
	if len(os.Args) < 2 {
		printMainHelp()
		return
	}

	// 2. SUBCOMMAND: user
	userCmd := flag.NewFlagSet("user", flag.ExitOnError)

	userCreate := userCmd.Bool("create", false, "create user")
	userDelete := userCmd.Bool("delete", false, "delete user")
	userName := userCmd.String("name", "", "user name (required)")
	userAge := userCmd.Int("age", 18, "user age")

	// 3. SUBCOMMAND: server
	serverCmd := flag.NewFlagSet("server", flag.ExitOnError)

	serverStart := serverCmd.Bool("start", false, "start server")
	serverPort := serverCmd.Int("port", 8080, "server port")
	serverEnv := serverCmd.String("env", "dev", "env (dev|prod)")

	// 4. SUBCOMMAND: math
	mathCmd := flag.NewFlagSet("math", flag.ExitOnError)

	add := mathCmd.Bool("add", false, "add numbers")
	mul := mathCmd.Bool("mul", false, "multiply numbers")

	// 5. SUBCOMMAND SWITCH
	switch os.Args[1] {

	// 6. USER SUBCOMMAND
	case "user":
		userCmd.Parse(os.Args[2:])

		if *userName == "" {
			fmt.Println("❌ -name is required")
			return
		}

		if *userCreate {
			fmt.Println("✅ Creating user:", *userName, "age:", *userAge)
		}

		if *userDelete {
			fmt.Println("🗑 Deleting user:", *userName)
		}

		fmt.Println("tail args:", userCmd.Args())

	// 7. SERVER SUBCOMMAND
	case "server":
		serverCmd.Parse(os.Args[2:])

		validEnv := map[string]bool{"dev": true, "prod": true}
		if !validEnv[*serverEnv] {
			fmt.Println("❌ invalid env")
			return
		}

		if *serverStart {
			fmt.Printf("🚀 Starting server on port %d (%s)\n", *serverPort, *serverEnv)
		}

	// 8. MATH SUBCOMMAND
	case "math":
		mathCmd.Parse(os.Args[2:])
		args := mathCmd.Args()

		if len(args) < 2 {
			fmt.Println("Provide numbers!")
			return
		}

		nums := toInts(args)

		if *add {
			fmt.Println("Sum =", sum(nums))
		}
		if *mul {
			fmt.Println("Product =", product(nums))
		}

	// 9. UNKNOWN SUBCOMMAND
	default:
		fmt.Println("Unknown command:", os.Args[1])
		printMainHelp()
	}

	// Global verbose behavior
	if *verbose {
		fmt.Println("🔎 verbose mode enabled")
	}
}

func printMainHelp() {
	fmt.Println("Usage:")
	fmt.Println("  app [global flags] <command> [flags]")
	fmt.Println("\nCommands:")
	fmt.Println("  user    manage users")
	fmt.Println("  server  manage server")
	fmt.Println("  math    math operations")
	fmt.Println("\nGlobal flags:")
	fmt.Println("  -v          verbose")
	fmt.Println("  -version    show version")
}

// helpers
func toInts(args []string) []int {
	var nums []int
	for _, a := range args {
		var n int
		fmt.Sscanf(a, "%d", &n)
		nums = append(nums, n)
	}
	return nums
}

func sum(nums []int) int {
	s := 0
	for _, n := range nums {
		s += n
	}
	return s
}

func product(nums []int) int {
	p := 1
	for _, n := range nums {
		p *= n
	}
	return p
}