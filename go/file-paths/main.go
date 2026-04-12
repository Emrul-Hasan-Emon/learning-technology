package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	// 1️. JOIN PATHS (OS SAFE)
	fmt.Println("===== JOIN PATHS =====")

	p := filepath.Join("dir1", "dir2", "filename.txt")
	fmt.Println("Joined:", p)

	fmt.Println(filepath.Join("dir1//", "filename"))
	fmt.Println(filepath.Join("dir1/../dir1", "filename"))

	// 2️. DIR & BASE
	fmt.Println("\n===== DIR & BASE =====")

	fmt.Println("Dir:", filepath.Dir(p))
	fmt.Println("Base:", filepath.Base(p))

	// 3️. ABSOLUTE vs RELATIVE PATHS
	fmt.Println("\n===== ABSOLUTE PATH CHECK =====")

	fmt.Println(filepath.IsAbs("dir/file"))
	fmt.Println(filepath.IsAbs("/dir/file"))

	abs, _ := filepath.Abs("myfile.txt")
	fmt.Println("Absolute path:", abs)

	// 4️. FILE EXTENSIONS
	fmt.Println("\n===== EXTENSIONS =====")

	filename := "config.json"

	ext := filepath.Ext(filename)
	fmt.Println("Extension:", ext)

	nameWithoutExt := strings.TrimSuffix(filename, ext)
	fmt.Println("Without ext:", nameWithoutExt)

	// 5️. RELATIVE PATH CALCULATION
	fmt.Println("\n===== RELATIVE PATH =====")

	rel, _ := filepath.Rel("a/b", "a/b/t/file.txt")
	fmt.Println(rel)

	rel, _ = filepath.Rel("a/b", "a/c/t/file.txt")
	fmt.Println(rel)

	// 6️. CLEAN PATH (IMPORTANT)
	fmt.Println("\n===== CLEAN PATH =====")

	dirty := "a/b/../c//./file.txt"
	clean := filepath.Clean(dirty)

	fmt.Println("Dirty:", dirty)
	fmt.Println("Clean:", clean)

	// 7️. SPLIT PATH
	fmt.Println("\n===== SPLIT PATH =====")

	dir, file := filepath.Split("/home/user/docs/file.txt")
	fmt.Println("Dir:", dir)
	fmt.Println("File:", file)

	// 8️. WALK DIRECTORY (VERY IMPORTANT)
	fmt.Println("\n===== WALK DIRECTORY =====")

	root := "."

	filepath.WalkDir(root, func(path string, d os.DirEntry, err error) error {
		if err != nil {
			return err
		}

		if d.IsDir() {
			fmt.Println("DIR :", path)
		} else {
			fmt.Println("FILE:", path)
		}
		return nil
	})

	// 9️. GLOB (SEARCH FILES)
	fmt.Println("\n===== GLOB SEARCH =====")

	matches, _ := filepath.Glob("*.go")
	fmt.Println("Go files:", matches)

	// 10. TEMP DIRECTORY
	fmt.Println("\n===== TEMP DIRECTORY =====")

	fmt.Println("Temp dir:", os.TempDir())

	// 11. BUILDING USER FILE PATHS (REAL WORLD)
	fmt.Println("\n===== REAL WORLD EXAMPLE =====")

	userID := "123"
	uploadDir := filepath.Join("uploads", userID, "profile")

	profilePic := filepath.Join(uploadDir, "avatar.png")

	fmt.Println("Upload dir:", uploadDir)
	fmt.Println("Profile pic:", profilePic)

	fmt.Println("\nDone 🚀")
}