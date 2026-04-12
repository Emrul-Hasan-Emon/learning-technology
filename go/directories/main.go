package main

import (
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
)

// Helper to handle errors quickly
func check(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	// 1️. CREATE A PROJECT DIRECTORY
	fmt.Println("Creating project workspace...")
	err := os.Mkdir("project", 0755)
	check(err)

	// Clean everything after program ends
	defer os.RemoveAll("project")

	// 2️. CREATE NESTED DIRECTORIES
	fmt.Println("Creating folder structure...")
	err = os.MkdirAll("project/src/utils", 0755)
	check(err)

	err = os.MkdirAll("project/assets/images", 0755)
	check(err)

	err = os.MkdirAll("project/docs", 0755)
	check(err)

	// 3️. CREATE & WRITE FILES
	fmt.Println("Creating files with content...")

	writeFile := func(path, content string) {
		err := os.WriteFile(path, []byte(content), 0644)
		check(err)
	}

	writeFile("project/README.md", "# My Go Project")
	writeFile("project/src/main.go", "package main\nfunc main(){}")
	writeFile("project/src/utils/helper.go", "package utils")
	writeFile("project/docs/guide.txt", "Project documentation")

	// 4️. READ DIRECTORY CONTENTS
	fmt.Println("\n📂 Listing project/src directory:")
	files, err := os.ReadDir("project/src")
	check(err)

	for _, f := range files {
		fmt.Println(" ", f.Name(), "IsDir:", f.IsDir())
	}

	// 5️. CHANGE WORKING DIRECTORY
	fmt.Println("\nChanging directory to project/docs...")
	err = os.Chdir("project/docs")
	check(err)

	files, err = os.ReadDir(".")
	check(err)

	fmt.Println("📂 Listing current directory (docs):")
	for _, f := range files {
		fmt.Println(" ", f.Name(), "IsDir:", f.IsDir())
	}

	// Go back to root
	err = os.Chdir("../..")
	check(err)

	// 6️. GET FILE INFO (STAT)
	info, err := os.Stat("project/README.md")
	check(err)

	fmt.Println("\n📄 File Info:")
	fmt.Println(" Name:", info.Name())
	fmt.Println(" Size:", info.Size())
	fmt.Println(" IsDir:", info.IsDir())

	// 7️. RENAME A FILE
	fmt.Println("\nRenaming README.md -> README_NEW.md")
	err = os.Rename("project/README.md", "project/README_NEW.md")
	check(err)

	// 8️. COPY FILE (manual copy example)
	fmt.Println("Copying README_NEW.md -> docs/copy.md")
	data, err := os.ReadFile("project/README_NEW.md")
	check(err)
	err = os.WriteFile("project/docs/copy.md", data, 0644)
	check(err)

	// 9️. WALK ENTIRE DIRECTORY TREE
	fmt.Println("\n🌲 Walking entire project directory:")
	filepath.WalkDir("project", visit)

	// 10. DELETE A SINGLE FILE
	fmt.Println("\nDeleting docs/copy.md")
	err = os.Remove("project/docs/copy.md")
	check(err)

	fmt.Println("\nProgram finished. Project folder will be deleted automatically.")
}

// Walk function
func visit(path string, d fs.DirEntry, err error) error {
	if err != nil {
		return err
	}
	fmt.Println(" ", path, "Dir:", d.IsDir())
	return nil
}