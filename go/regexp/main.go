package main

import (
	"bytes"
	"fmt"
	"regexp"
)

func main() {

	// ------------------------------------------------------------
	// 1️. BASIC MATCHING
	// ------------------------------------------------------------
	fmt.Println("===== BASIC MATCH =====")

	match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
	fmt.Println("MatchString:", match)

	r := regexp.MustCompile("p([a-z]+)ch")

	fmt.Println("MatchString:", r.MatchString("peach"))

	// ------------------------------------------------------------
	// 2️. FIND FIRST MATCH
	// ------------------------------------------------------------
	fmt.Println("\n===== FIND FIRST MATCH =====")

	fmt.Println("FindString:", r.FindString("peach punch"))

	// ------------------------------------------------------------
	// 3️. INDEX LOCATION
	// ------------------------------------------------------------
	fmt.Println("\n===== INDEX =====")

	fmt.Println("FindStringIndex:", r.FindStringIndex("peach punch"))

	// ------------------------------------------------------------
	// 4️. SUBMATCH EXTRACTION
	// ------------------------------------------------------------
	fmt.Println("\n===== SUBMATCH =====")

	fmt.Println("FindStringSubmatch:", r.FindStringSubmatch("peach punch"))

	fmt.Println("FindStringSubmatchIndex:", r.FindStringSubmatchIndex("peach punch"))

	// ------------------------------------------------------------
	// 5️. FIND ALL MATCHES
	// ------------------------------------------------------------
	fmt.Println("\n===== FIND ALL =====")

	fmt.Println(r.FindAllString("peach punch pinch", -1))

	fmt.Println("FindAllSubmatchIndex:",
		r.FindAllStringSubmatchIndex("peach punch pinch", -1))

	fmt.Println("Limit 2 matches:",
		r.FindAllString("peach punch pinch", 2))

	// ------------------------------------------------------------
	// 6️. BYTE INPUT MATCHING
	// ------------------------------------------------------------
	fmt.Println("\n===== BYTE MATCH =====")

	fmt.Println("Match bytes:", r.Match([]byte("peach")))

	// ------------------------------------------------------------
	// 7️. REPLACE OPERATIONS
	// ------------------------------------------------------------
	fmt.Println("\n===== REPLACE =====")

	r = regexp.MustCompile("p([a-z]+)ch")

	fmt.Println("ReplaceAllString:",
		r.ReplaceAllString("a peach is a punch", "<fruit>"))

	// Replace with captured group
	fmt.Println("ReplaceAllStringFunc:",
		r.ReplaceAllStringFunc("peach punch pinch", func(s string) string {
			return "[" + s + "]"
		}))

	// ------------------------------------------------------------
	// 8️. FUNCTION BASED REPLACE (ADVANCED)
	// ------------------------------------------------------------
	fmt.Println("\n===== REPLACE ALL FUNC (bytes) =====")

	in := []byte("a peach punch")

	out := r.ReplaceAllFunc(in, bytes.ToUpper)
	fmt.Println(string(out))

	// ------------------------------------------------------------
	// 9️. SPLIT STRING USING REGEX
	// ------------------------------------------------------------
	fmt.Println("\n===== SPLIT =====")

	splitR := regexp.MustCompile(`[,\s]+`) // split by comma or space

	words := splitR.Split("go, rust  java  python", -1)
	fmt.Println(words)

	// ------------------------------------------------------------
	// 10. VALIDATION PATTERNS (REAL WORLD)
	// ------------------------------------------------------------

	fmt.Println("\n===== VALIDATION =====")

	emailRegex := regexp.MustCompile(`^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$`)
	fmt.Println("Email valid:",
		emailRegex.MatchString("test@example.com"))

	phoneRegex := regexp.MustCompile(`^\+?[0-9]{10,13}$`)
	fmt.Println("Phone valid:",
		phoneRegex.MatchString("+8801712345678"))

	// ------------------------------------------------------------
	// 11. EXTRACT GROUPS (REAL PARSING CASE)
	// ------------------------------------------------------------

	fmt.Println("\n===== GROUP EXTRACTION =====")

	log := "ERROR 2024: database failed at 10:30"

	logRegex := regexp.MustCompile(`(ERROR|INFO|WARN)\s+([0-9]{4}): (.+)`)

	matches := logRegex.FindStringSubmatch(log)

	if len(matches) > 0 {
		fmt.Println("Level:", matches[1])
		fmt.Println("Year:", matches[2])
		fmt.Println("Message:", matches[3])
	}

	// ------------------------------------------------------------
	// 12. GREEDY vs NON-GREEDY
	// ------------------------------------------------------------

	fmt.Println("\n===== GREEDY VS NON-GREEDY =====")

	text := "<b>Go</b> <b>Rust</b>"

	greedy := regexp.MustCompile(`<b>.*</b>`)
	nonGreedy := regexp.MustCompile(`<b>.*?</b>`)

	fmt.Println("Greedy:", greedy.FindString(text))
	fmt.Println("Non-Greedy:", nonGreedy.FindAllString(text, -1))

	// ------------------------------------------------------------
	// 13. CASE INSENSITIVE MATCH
	// ------------------------------------------------------------

	fmt.Println("\n===== CASE INSENSITIVE =====")

	ci := regexp.MustCompile(`(?i)go`)

	fmt.Println(ci.FindAllString("Go gO GO go", -1))
}