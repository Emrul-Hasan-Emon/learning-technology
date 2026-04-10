package main

import (
	"fmt"
	"strings"
	"unicode"
	"unicode/utf8"
)

func main() {

	//---------------------------------------------------
	// 1. Strings are byte slices (UTF-8 encoded)
	//---------------------------------------------------
	const s = "สวัสดี" // Thai word

	fmt.Println("String:", s)

	// length = number of BYTES (not characters!)
	fmt.Println("Byte length:", len(s))

	//---------------------------------------------------
	// 2. Access raw bytes
	//---------------------------------------------------
	fmt.Println("\nBytes (hex):")
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
	fmt.Println()

	//---------------------------------------------------
	// 3. Rune count (actual characters)
	//---------------------------------------------------
	fmt.Println("\nRune count:", utf8.RuneCountInString(s))

	//---------------------------------------------------
	// 4. Range loop automatically decodes runes
	//---------------------------------------------------
	fmt.Println("\nUsing range loop:")
	for index, runeValue := range s {
		fmt.Printf("%#U starts at byte index %d\n", runeValue, index)
	}

	//---------------------------------------------------
	// 5. Manual rune decoding
	//---------------------------------------------------
	fmt.Println("\nManual DecodeRuneInString:")
	for i := 0; i < len(s); {
		r, size := utf8.DecodeRuneInString(s[i:])
		fmt.Printf("%#U starts at %d (size %d bytes)\n", r, i, size)
		i += size
		examineRune(r)
	}

	//---------------------------------------------------
	// 6. String concatenation
	//---------------------------------------------------
	a := "Hello"
	b := "World"
	fmt.Println("\nConcatenation:", a+" "+b)

	//---------------------------------------------------
	// 7. String comparison
	//---------------------------------------------------
	fmt.Println("Equal?", a == "Hello")

	//---------------------------------------------------
	// 8. Multi-line strings (Raw string literal)
	//---------------------------------------------------
	raw := `This is
a multi-line
string`
	fmt.Println("\nRaw string:\n", raw)

	//---------------------------------------------------
	// 9. String immutability
	//---------------------------------------------------
	str := "Go"
	// str[0] = 'N' ❌ ERROR (strings are immutable)

	// To modify → convert to []rune or []byte
	runes := []rune(str)
	runes[0] = 'N'
	str = string(runes)
	fmt.Println("\nModified string:", str)

	//---------------------------------------------------
	// 10. Strings package functions
	//---------------------------------------------------
	text := "  golang is awesome  "

	fmt.Println("\nUpper:", strings.ToUpper(text))
	fmt.Println("Lower:", strings.ToLower(text))
	fmt.Println("Trim:", strings.TrimSpace(text))
	fmt.Println("Contains 'go':", strings.Contains(text, "go"))
	fmt.Println("Replace:", strings.ReplaceAll(text, "awesome", "great"))

	//---------------------------------------------------
	// 11. Split & Join
	//---------------------------------------------------
	words := strings.Split("a,b,c,d", ",")
	fmt.Println("\nSplit:", words)

	joined := strings.Join(words, "-")
	fmt.Println("Join:", joined)

	//---------------------------------------------------
	// 12. Rune utilities (unicode package)
	//---------------------------------------------------
	ch := 'A'
	fmt.Println("\nIsLetter:", unicode.IsLetter(ch))
	fmt.Println("IsDigit:", unicode.IsDigit(ch))
	fmt.Println("ToLower:", string(unicode.ToLower(ch)))

	//---------------------------------------------------
	// 13. Build strings efficiently (String Builder)
	//---------------------------------------------------
	var builder strings.Builder
	builder.WriteString("Hello ")
	builder.WriteString("Go ")
	builder.WriteString("World")

	fmt.Println("\nString Builder:", builder.String())

	//---------------------------------------------------
	// 14. Iterate byte vs rune difference demo
	//---------------------------------------------------
	fmt.Println("\nByte iteration vs Rune iteration")

	word := "Go😊"

	fmt.Println("Byte iteration:")
	for i := 0; i < len(word); i++ {
		fmt.Printf("%x ", word[i])
	}

	fmt.Println("\nRune iteration:")
	for _, r := range word {
		fmt.Printf("%c ", r)
	}
}

////////////////////////////////////////////////////////
// Rune inspection helper
////////////////////////////////////////////////////////

func examineRune(r rune) {
	if r == 'ส' {
		fmt.Println("found Thai character 'so sua'")
	}
}