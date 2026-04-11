package main

import (
	"os"
	"text/template"
)

func main() {

	// 1️. BASIC TEMPLATE CREATION + PARSING
	// Create a new template named "t1"
	t1 := template.New("t1")

	// Parse a simple template string
	t1, err := t1.Parse("Value is {{.}}\n")
	if err != nil {
		panic(err)
	}

	// Must() is a helper that panics if parsing fails
	// We override / extend the template safely
	t1 = template.Must(t1.Parse("Value: {{.}}\n"))

	// 2️. Execute templates with different data types

	// 1. Simple string input
	t1.Execute(os.Stdout, "some text")

	// 2. Integer input
	t1.Execute(os.Stdout, 5)

	// 3. Slice input (iterated using {{range}})
	t1.Execute(os.Stdout, []string{
		"Go",
		"Rust",
		"C++",
		"C#",
	})

	// 2️. TEMPLATE FACTORY HELPER (REAL WORLD PATTERN)
	Create := func(name, tpl string) *template.Template {
		return template.Must(template.New(name).Parse(tpl))
	}

	// Template accessing struct fields
	t2 := Create("t2", "Name: {{.Name}}\n")

	// STRUCT DATA INPUT
	t2.Execute(os.Stdout, struct {
		Name string
	}{
		"Jane Doe",
	})

	// MAP DATA INPUT (dynamic fields)
	t2.Execute(os.Stdout, map[string]string{
		"Name": "Mickey Mouse",
	})

	// 3️. CONDITIONAL TEMPLATE (if / else)
	t3 := Create("t3",
		`{{if .}}YES: Value exists -> {{.}}{{else}}NO: empty value{{end}}\n`,
	)

	// non-empty value
	t3.Execute(os.Stdout, "not empty")

	// empty value
	t3.Execute(os.Stdout, "")

	// 4️. LOOPING (range over slice)
	t4 := Create("t4",
		`Languages: {{range .}}[{{.}}] {{end}}\n`,
	)

	t4.Execute(os.Stdout,
		[]string{
			"Go",
			"Rust",
			"C++",
			"C#",
		})

	// 5️. REAL WORLD TEMPLATE (STRUCTURED OUTPUT)
	type User struct {
		Name string
		Age  int
	}

	t5 := Create("t5",
		`User Profile:
		Name: {{.Name}}
		Age : {{.Age}}
		`,
			)

	t5.Execute(os.Stdout, User{
		Name: "Alice",
		Age:  25,
	})

	// 6️. MAP VS STRUCT FLEXIBILITY
	t6 := Create("t6",
		`Hello {{.Name}}! Welcome to {{.Platform}}\n`,
	)

	t6.Execute(os.Stdout, map[string]string{
		"Name":     "Developer",
		"Platform": "Go Templates",
	})

	// 7️. PIPELINE STYLE (data transformation chain)
	t7 := Create("t7",
		`Uppercase name: {{. | printf "%s" | len}}\n`,
	)

	t7.Execute(os.Stdout, "golang")

	// 8️. MULTI-LINE TEMPLATE (real-world email style)
	t8 := Create("t8",
		`
Hello {{.Name}},

Welcome to our platform.
Your account age: {{.Age}} years.

Thanks,
Team
`,
	)

	t8.Execute(os.Stdout, User{
		Name: "Bob",
		Age:  30,
	})
}