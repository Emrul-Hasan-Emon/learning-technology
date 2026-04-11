package main

import (
	"fmt"
	"strconv"
)

func main() {

	// ------------------------------------------------------------
	// 1️. STRING → FLOAT
	// ------------------------------------------------------------
	fmt.Println("===== STRING TO FLOAT =====")

	f, err := strconv.ParseFloat("1.234", 64)
	fmt.Println("float:", f, "error:", err)

	// ------------------------------------------------------------
	// 2️. STRING → INT (base auto-detect)
	// ------------------------------------------------------------
	fmt.Println("\n===== STRING TO INT =====")

	i, err := strconv.ParseInt("123", 0, 64)
	fmt.Println("int:", i, "error:", err)

	// ------------------------------------------------------------
	// 3️. HEX STRING → INT
	// ------------------------------------------------------------
	fmt.Println("\n===== HEX TO INT =====")

	hexVal, err := strconv.ParseInt("0x1c8", 0, 64)
	fmt.Println("hex (0x1c8):", hexVal, "error:", err)

	// ------------------------------------------------------------
	// 4️. STRING → UNSIGNED INT
	// ------------------------------------------------------------
	fmt.Println("\n===== STRING TO UINT =====")

	u, err := strconv.ParseUint("789", 0, 64)
	fmt.Println("uint:", u, "error:", err)

	// ------------------------------------------------------------
	// 5️. ATOI (MOST COMMON)
	// ------------------------------------------------------------
	fmt.Println("\n===== ATOI =====")

	k, err := strconv.Atoi("135")
	fmt.Println("atoi:", k, "error:", err)

	// ------------------------------------------------------------
	// 6️. INVALID INPUT HANDLING
	// ------------------------------------------------------------
	fmt.Println("\n===== ERROR CASE =====")

	_, e := strconv.Atoi("wat")
	fmt.Println("error:", e)

	// ------------------------------------------------------------
	// 7️. INT → STRING CONVERSION
	// ------------------------------------------------------------
	fmt.Println("\n===== INT TO STRING =====")

	num := 500
	str := strconv.Itoa(num)
	fmt.Println("string:", str)

	// ------------------------------------------------------------
	// 8️. FLOAT → STRING
	// ------------------------------------------------------------
	fmt.Println("\n===== FLOAT TO STRING =====")

	f2 := 3.14159
	strFloat := strconv.FormatFloat(f2, 'f', 2, 64)
	fmt.Println("float string:", strFloat)

	// ------------------------------------------------------------
	// 9️. INT → STRING (different bases)
	// ------------------------------------------------------------
	fmt.Println("\n===== BASE CONVERSIONS =====")

	n := int64(255)

	fmt.Println("binary:", strconv.FormatInt(n, 2))
	fmt.Println("octal:", strconv.FormatInt(n, 8))
	fmt.Println("decimal:", strconv.FormatInt(n, 10))
	fmt.Println("hex:", strconv.FormatInt(n, 16))

	// ------------------------------------------------------------
	// 10. BOOL ↔ STRING
	// ------------------------------------------------------------
	fmt.Println("\n===== BOOL CONVERSION =====")

	b, _ := strconv.ParseBool("true")
	fmt.Println("parsed bool:", b)

	fmt.Println("bool to string:", strconv.FormatBool(false))

	// ------------------------------------------------------------
	// 11. REAL WORLD: QUERY PARAM PARSING
	// ------------------------------------------------------------
	fmt.Println("\n===== QUERY PARAM STYLE =====")

	queryAge := "25"
	age, err := strconv.Atoi(queryAge)
	if err != nil {
		fmt.Println("invalid age")
	} else {
		fmt.Println("age:", age)
	}

	// ------------------------------------------------------------
	// 12. SAFE PARSING PATTERN (IMPORTANT)
	// ------------------------------------------------------------
	fmt.Println("\n===== SAFE PARSING =====")

	inputs := []string{"10", "20", "abc", "30"}

	for _, v := range inputs {
		val, err := strconv.Atoi(v)
		if err != nil {
			fmt.Println("invalid:", v)
			continue
		}
		fmt.Println("valid number:", val)
	}
}