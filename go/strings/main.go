package main

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

func main() {

	// 1️. BASIC STRING CREATION
	fmt.Println("===== BASIC STRINGS =====")

	s1 := "Hello"
	s2 := "World"

	fmt.Println("s1:", s1)
	fmt.Println("s2:", s2)

	// 2️. CONCATENATION
	fmt.Println("\n===== CONCATENATION =====")

	// using +
	s3 := s1 + " " + s2
	fmt.Println("plus:", s3)

	// using fmt.Sprintf
	s4 := fmt.Sprintf("%s %s!", s1, s2)
	fmt.Println("sprintf:", s4)

	// using strings.Builder (BEST for performance)
	var builder strings.Builder
	builder.WriteString(s1)
	builder.WriteString(" ")
	builder.WriteString(s2)

	fmt.Println("builder:", builder.String())

	// 3️. LENGTH & INDEXING
	fmt.Println("\n===== LENGTH & INDEXING =====")

	str := "GoLang"

	fmt.Println("string:", str)
	fmt.Println("length (bytes):", len(str))

	fmt.Println("byte at index 0:", str[0]) // byte value

	// 4️. UTF-8 / RUNES (IMPORTANT FOR NON-ASCII TEXT)
	fmt.Println("\n===== UTF-8 / RUNES =====")

	unicodeStr := "สวัสดี" // Thai greeting

	fmt.Println("string:", unicodeStr)
	fmt.Println("byte length:", len(unicodeStr))
	fmt.Println("rune count:", utf8.RuneCountInString(unicodeStr))

	// iterate over runes (correct way)
	for i, r := range unicodeStr {
		fmt.Printf("index %d => rune %c\n", i, r)
	}

	// 5️. SUBSTRING / SLICING
	fmt.Println("\n===== SLICING =====")

	text := "HelloGoLang"

	fmt.Println("text:", text)
	fmt.Println("substring (0-5):", text[0:5])
	fmt.Println("substring (5-end):", text[5:])

	// 6️. COMPARISON
	fmt.Println("\n===== COMPARISON =====")

	a := "apple"
	b := "banana"

	fmt.Println("a == b:", a == b)
	fmt.Println("a < b:", a < b) // lexicographical order

	// 7️. SEARCH OPERATIONS
	fmt.Println("\n===== SEARCH =====")

	s := "go is powerful go language"

	fmt.Println("contains 'go':", strings.Contains(s, "go"))
	fmt.Println("count 'go':", strings.Count(s, "go"))
	fmt.Println("index of 'powerful':", strings.Index(s, "powerful"))
	fmt.Println("has prefix 'go':", strings.HasPrefix(s, "go"))
	fmt.Println("has suffix 'language':", strings.HasSuffix(s, "language"))

	// 8️. REPLACE
	fmt.Println("\n===== REPLACE =====")

	str2 := "I like Java, Java is great"

	fmt.Println("original:", str2)

	replaced := strings.ReplaceAll(str2, "Java", "Go")
	fmt.Println("replaced:", replaced)

	// 9️. SPLIT
	fmt.Println("\n===== SPLIT =====")

	csv := "apple,banana,mango,grape"

	parts := strings.Split(csv, ",")

	fmt.Println("split result:")
	for i, p := range parts {
		fmt.Println(i, "=>", p)
	}

	// 10. JOIN
	fmt.Println("\n===== JOIN =====")

	joined := strings.Join(parts, " | ")
	fmt.Println("joined:", joined)

	// 11. TRIM (whitespace removal)
	fmt.Println("\n===== TRIM =====")

	raw := "   hello go   "

	fmt.Println("raw:", raw)
	fmt.Println("trimmed:", strings.TrimSpace(raw))

	// custom trim
	raw2 := "***hello***"
	fmt.Println("custom trim:", strings.Trim(raw2, "*"))

	// 1️2. CASE CONVERSION
	fmt.Println("\n===== CASE =====")

	msg := "Go Lang"

	fmt.Println("upper:", strings.ToUpper(msg))
	fmt.Println("lower:", strings.ToLower(msg))

	// 1️3. STRING BUILDING LOOP (PERFORMANCE IMPORTANT)
	fmt.Println("\n===== STRING BUILDER LOOP =====")

	var bld strings.Builder

	for i := 0; i < 5; i++ {
		bld.WriteString("go ")
	}

	fmt.Println("built string:", bld.String())

	// 1️4. STRING ITERATION BYTE VS RUNE
	fmt.Println("\n===== BYTE VS RUNE =====")

	word := "Go🚀"

	fmt.Println("byte iteration:")
	for i := 0; i < len(word); i++ {
		fmt.Printf("%x ", word[i])
	}
	fmt.Println()

	fmt.Println("rune iteration:")
	for _, r := range word {
		fmt.Printf("%c ", r)
	}
	fmt.Println()
}