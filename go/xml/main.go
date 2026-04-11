package main

import (
	"encoding/xml"
	"fmt"
)

// BASIC STRUCT MAPPING TO XML
type Plant struct {

	// Root XML element name: <plant>
	XMLName xml.Name `xml:"plant"`

	// Attribute: <plant id="27">
	Id int `xml:"id,attr"`

	// Simple element: <name>Coffee</name>
	Name string `xml:"name"`

	// Repeated elements:
	// <origin>Ethiopia</origin>
	// <origin>Brazil</origin>
	Origin []string `xml:"origin"`
}

// Stringer for pretty printing
func (p Plant) String() string {
	return fmt.Sprintf("Plant id=%v, name=%v, origin=%v",
		p.Id, p.Name, p.Origin)
}

func main() {

	// 1️. STRUCT → XML (MARSHAL)
	fmt.Println("===== MARSHAL STRUCT TO XML =====")

	coffee := &Plant{
		Id:     27,
		Name:   "Coffee",
		Origin: []string{"Ethiopia", "Brazil"},
	}

	out, err := xml.MarshalIndent(coffee, " ", "  ")
	if err != nil {
		panic(err)
	}

	fmt.Println(string(out))

	// Add XML header (important for real XML documents)
	fmt.Println(xml.Header + string(out))

	// 2️. XML → STRUCT (UNMARSHAL)
	fmt.Println("\n===== UNMARSHAL XML =====")

	var p Plant

	if err := xml.Unmarshal(out, &p); err != nil {
		panic(err)
	}

	fmt.Println("decoded struct:", p)

	// 3️. MULTIPLE STRUCTS (NESTED XML)
	fmt.Println("\n===== NESTED XML STRUCTURE =====")

	tomato := &Plant{
		Id:     81,
		Name:   "Tomato",
		Origin: []string{"Mexico", "California"},
	}

	// Nested XML structure:
	// <nesting>
	//   <parent>
	//     <child>
	//       <plant>...</plant>
	//     </child>
	//   </parent>
	// </nesting>
	// ------------------------------------------------------------
	type Nesting struct {
		XMLName xml.Name `xml:"nesting"`
		Plants  []*Plant `xml:"parent>child>plant"`
	}

	nesting := &Nesting{
		Plants: []*Plant{coffee, tomato},
	}

	nestedXML, err := xml.MarshalIndent(nesting, " ", "  ")
	if err != nil {
		panic(err)
	}

	fmt.Println(string(nestedXML))

	// 4️. XML WITH ATTRIBUTES VS ELEMENTS
	fmt.Println("\n===== ATTRIBUTES VS ELEMENTS =====")

	type Book struct {
		XMLName xml.Name `xml:"book"`
		ID      int      `xml:"id,attr"`     // attribute
		Title   string   `xml:"title"`       // element
		Author  string   `xml:"author"`      // element
	}

	book := Book{
		ID:     101,
		Title:  "Go Programming",
		Author: "John Doe",
	}

	bookXML, _ := xml.MarshalIndent(book, "", "  ")
	fmt.Println(string(bookXML))

	// 5️. XML LIST (ARRAY HANDLING)
	fmt.Println("\n===== LIST HANDLING =====")

	type Library struct {
		XMLName xml.Name `xml:"library"`
		Plants  []Plant  `xml:"plant"`
	}

	lib := Library{
		Plants: []Plant{
			{Id: 1, Name: "Rose"},
			{Id: 2, Name: "Lily"},
		},
	}

	libXML, _ := xml.MarshalIndent(lib, "", "  ")
	fmt.Println(string(libXML))

	// 6️. REAL-WORLD API STYLE XML RESPONSE
	fmt.Println("\n===== API STYLE XML =====")

	type Response struct {
		XMLName xml.Name `xml:"response"`
		Status  string   `xml:"status"`
		Data    string   `xml:"data"`
	}

	resp := Response{
		Status: "success",
		Data:   "Plants loaded",
	}

	respXML, _ := xml.MarshalIndent(resp, "", "  ")
	fmt.Println(xml.Header + string(respXML))
}