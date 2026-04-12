package main

import (
	"flag"
	"fmt"
	"os"
	"strings"
	"time"
)

func main() {

	fmt.Println("===== BASIC FLAGS =====")

	// 1️. Basic pointer flags
	wordPtr := flag.String("word", "foo", "a string flag")
	numbPtr := flag.Int("numb", 42, "an int flag")
	forkPtr := flag.Bool("fork", false, "a bool flag")
	floatPtr := flag.Float64("price", 99.9, "a float flag")

	// 2️. StringVar / IntVar / BoolVar (store directly into variables)
	var name string
	var age int
	var isAdmin bool

	flag.StringVar(&name, "name", "Guest", "user name")
	flag.IntVar(&age, "age", 18, "user age")
	flag.BoolVar(&isAdmin, "admin", false, "admin user")

	// 3️. Duration flag
	timeout := flag.Duration("timeout", time.Second*5, "timeout duration")

	// 4️. Custom usage message
	flag.Usage = func() {
		fmt.Println("🚀 Custom CLI Usage")
		fmt.Println("Example:")
		fmt.Println("./app -word=hello -numb=10 -admin=true file1 file2")
		fmt.Println("\nAvailable flags:")
		flag.PrintDefaults()
	}

	flag.Parse()

	fmt.Println("\n===== PARSED FLAG VALUES =====")
	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:", *numbPtr)
	fmt.Println("fork:", *forkPtr)
	fmt.Println("price:", *floatPtr)
	fmt.Println("name:", name)
	fmt.Println("age:", age)
	fmt.Println("admin:", isAdmin)
	fmt.Println("timeout:", *timeout)

	// Remaining non-flag arguments
	fmt.Println("tail args:", flag.Args())

	// First non-flag argument shortcut
	if flag.NArg() > 0 {
		fmt.Println("first tail arg:", flag.Arg(0))
	}

	fmt.Println("\n===== FLAG DETECTION =====")

	// 5️. Check if flag was explicitly set
	flag.Visit(func(f *flag.Flag) {
		fmt.Println("Flag provided by user:", f.Name)
	})

	fmt.Println("\n===== REQUIRED FLAG EXAMPLE =====")

	// 6️. Simulate required flag
	if name == "Guest" {
		fmt.Println("❌ -name flag is required")
		// os.Exit(1)   // normally you'd exit
	}

	fmt.Println("\n===== ENUM / VALIDATION EXAMPLE =====")

	env := flag.String("env", "dev", "environment (dev|prod|staging)")
	flag.Parse()

	validEnv := map[string]bool{"dev": true, "prod": true, "staging": true}
	if !validEnv[*env] {
		fmt.Println("Invalid env value!")
	}

	fmt.Println("\n===== REPEATED FLAG (LIST) EXAMPLE =====")

	// Custom slice flag
	var langs stringSlice
	flag.Var(&langs, "lang", "repeatable language flag")
	flag.Parse()

	fmt.Println("Languages:", langs)

	fmt.Println("\n===== SUBCOMMAND STYLE FLAGS =====")

	if len(os.Args) > 1 {
		switch os.Args[1] {
		case "serve":
			fmt.Println("Running server...")
		case "build":
			fmt.Println("Building project...")
		}
	}

	fmt.Println("\nProgram finished 🎉")
}

//// Custom flag type (slice support)
type stringSlice []string

func (s *stringSlice) String() string {
	return strings.Join(*s, ",")
}

func (s *stringSlice) Set(value string) error {
	*s = append(*s, value)
	return nil
}

// go build main.go

/**
$ ./main -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []

$ ./main -word=opt
word: opt
numb: 42
fork: false
svar: bar
tail: []

$ ./main -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

$ ./main -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

$ ./main -h
Usage of ./command-line-flags:
-fork=false: a bool
-numb=42: an int
-svar="bar": a string var
-word="foo": a string

$ ./main -wat
flag provided but not defined: -wat
Usage of ./command-line-flags:
*/