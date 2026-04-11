package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

// ------------------------------------------------------------
// STRUCTS FOR JSON MARSHAL / UNMARSHAL
// ------------------------------------------------------------

// No tags → JSON uses field names as-is (capitalized)
type response1 struct {
	Page   int
	Fruits []string
}

// With JSON tags → control JSON keys
type response2 struct {
	Page   int      `json:"page"`
	Fruits []string `json:"fruits"`
}

func main() {

	// 1️. BASIC JSON MARSHAL (Go → JSON)
	fmt.Println("===== BASIC MARSHAL =====")

	bolB, _ := json.Marshal(true)
	fmt.Println("bool:", string(bolB))

	intB, _ := json.Marshal(1)
	fmt.Println("int:", string(intB))

	fltB, _ := json.Marshal(2.34)
	fmt.Println("float:", string(fltB))

	strB, _ := json.Marshal("gopher")
	fmt.Println("string:", string(strB))

	// 2️. SLICE → JSON ARRAY
	fmt.Println("\n===== SLICE MARSHAL =====")

	slcD := []string{"apple", "peach", "pear"}
	slcB, _ := json.Marshal(slcD)
	fmt.Println(string(slcB))

	// 3️. MAP → JSON OBJECT
	fmt.Println("\n===== MAP MARSHAL =====")

	mapD := map[string]int{"apple": 5, "lettuce": 7}
	mapB, _ := json.Marshal(mapD)
	fmt.Println(string(mapB))

	// 4️. STRUCT → JSON (NO TAGS)
	fmt.Println("\n===== STRUCT (NO TAGS) =====")

	res1D := &response1{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"},
	}

	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	// 5️. STRUCT → JSON (WITH TAGS)
	fmt.Println("\n===== STRUCT (WITH TAGS) =====")

	res2D := &response2{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"},
	}

	res2B, _ := json.Marshal(res2D)
	fmt.Println(string(res2B))

	// 6️. JSON → MAP (DYNAMIC STRUCTURE)
	fmt.Println("\n===== UNMARSHAL TO MAP =====")

	byt := []byte(`{"num":6.13,"strs":["a","b"]}`)

	var dat map[string]interface{}

	if err := json.Unmarshal(byt, &dat); err != nil {
		panic(err)
	}

	fmt.Println("map:", dat)

	// Type assertions (VERY IMPORTANT)
	num := dat["num"].(float64)
	fmt.Println("num:", num)

	strs := dat["strs"].([]interface{})
	str1 := strs[0].(string)
	fmt.Println("first string:", str1)

	// 7️. JSON → STRUCT (STRONG TYPING)
	fmt.Println("\n===== UNMARSHAL TO STRUCT =====")

	str := `{"page": 1, "fruits": ["apple", "peach"]}`

	res := response2{}

	json.Unmarshal([]byte(str), &res)

	fmt.Println("struct:", res)
	fmt.Println("first fruit:", res.Fruits[0])

	// 8️. JSON ENCODER (STREAMING OUTPUT)
	fmt.Println("\n===== ENCODER =====")

	enc := json.NewEncoder(os.Stdout)

	d := map[string]int{"apple": 5, "lettuce": 7}

	enc.Encode(d)

	// 9️. JSON DECODER (STREAMING INPUT)
	fmt.Println("\n===== DECODER =====")

	dec := json.NewDecoder(strings.NewReader(str))

	res1 := response2{}

	dec.Decode(&res1)

	fmt.Println("decoded struct:", res1)

	// 10. REAL-WORLD API RESPONSE STYLE
	fmt.Println("\n===== API STYLE RESPONSE =====")

	type User struct {
		ID    int      `json:"id"`
		Name  string   `json:"name"`
		Email string   `json:"email"`
		Tags  []string `json:"tags"`
	}

	user := User{
		ID:    101,
		Name:  "Alice",
		Email: "alice@example.com",
		Tags:  []string{"admin", "developer"},
	}

	jsonBytes, _ := json.MarshalIndent(user, "", "  ")

	fmt.Println(string(jsonBytes))
}