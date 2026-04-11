package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"path/filepath"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {

	// 1️. FILE PATH CREATION
	fmt.Println("===== FILE PATH =====")

	path := filepath.Join(os.TempDir(), "dat")
	fmt.Println("file path:", path)

	// 2️. READ ENTIRE FILE (SIMPLE METHOD)
	fmt.Println("\n===== READ ALL =====")

	dat, err := os.ReadFile(path)
	check(err)

	fmt.Println("content:")
	fmt.Println(string(dat))

	// 3️. OPEN FILE (STREAMING MODE)
	fmt.Println("\n===== OPEN FILE =====")

	f, err := os.Open(path)
	check(err)
	defer f.Close()

	// 4️. READ FIXED BYTES
	fmt.Println("\n===== READ BYTES =====")

	b1 := make([]byte, 5)
	n1, err := f.Read(b1)
	check(err)

	fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))

	// 5️. SEEKING (MOVE CURSOR)
	fmt.Println("\n===== SEEK OPERATIONS =====")

	// Move to position 6 from start
	o2, err := f.Seek(6, io.SeekStart)
	check(err)

	b2 := make([]byte, 2)
	n2, err := f.Read(b2)
	check(err)

	fmt.Printf("%d bytes @ %d: %s\n", n2, o2, string(b2[:n2]))

	// Move relative to current position
	_, err = f.Seek(2, io.SeekCurrent)
	check(err)

	// Move relative to end
	_, err = f.Seek(-4, io.SeekEnd)
	check(err)

	// 6️. READ AT LEAST (ENSURES FULL READ)
	fmt.Println("\n===== READ AT LEAST =====")

	o3, err := f.Seek(6, io.SeekStart)
	check(err)

	b3 := make([]byte, 2)
	n3, err := io.ReadAtLeast(f, b3, 2)
	check(err)

	fmt.Printf("%d bytes @ %d: %s\n", n3, o3, string(b3))

	// 7️. RESET FILE CURSOR
	fmt.Println("\n===== RESET CURSOR =====")

	_, err = f.Seek(0, io.SeekStart)
	check(err)

	// 8️. BUFFERED READING (FAST IO)
	fmt.Println("\n===== BUFFERED READER =====")

	reader := bufio.NewReader(f)

	b4, err := reader.Peek(5)
	check(err)

	fmt.Println("peek 5 bytes:", string(b4))

	// 9️. REAL WORLD: LINE BY LINE READING
	fmt.Println("\n===== LINE BY LINE =====")

	_, err = f.Seek(0, io.SeekStart)
	check(err)

	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		fmt.Println("line:", scanner.Text())
	}

	check(scanner.Err())

	// 10. REAL WORLD: STREAM COPY (FILE PIPELINE)
	fmt.Println("\n===== STREAM COPY =====")

	_, err = f.Seek(0, io.SeekStart)
	check(err)

	dst := filepath.Join(os.TempDir(), "copy.dat")

	outFile, err := os.Create(dst)
	check(err)
	defer outFile.Close()

	_, err = io.Copy(outFile, f)
	check(err)

	fmt.Println("file copied to:", dst)

	// 11. FILE STAT INFO
	fmt.Println("\n===== FILE INFO =====")

	info, err := os.Stat(path)
	check(err)

	fmt.Println("size:", info.Size())
	fmt.Println("is dir:", info.IsDir())
	fmt.Println("mod time:", info.ModTime())

	// 12. SAFETY NOTE
	fmt.Println("\n===== SAFETY NOTE =====")

	fmt.Println("Always check errors in file I/O")
	fmt.Println("Always close files using defer")
}