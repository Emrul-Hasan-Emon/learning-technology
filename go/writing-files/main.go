package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {

	// 1. SIMPLE WRITE (OVERWRITE FILE)
	fmt.Println("===== SIMPLE WRITE =====")

	data := []byte("hello\ngo\n")

	path1 := filepath.Join(os.TempDir(), "dat1")

	err := os.WriteFile(path1, data, 0644)
	check(err)

	fmt.Println("written file:", path1)

	// 2. CREATE FILE + WRITE BYTES
	fmt.Println("\n===== CREATE + WRITE BYTES =====")

	path2 := filepath.Join(os.TempDir(), "dat2")

	f, err := os.Create(path2)
	check(err)
	defer f.Close()

	d2 := []byte{115, 111, 109, 101, 10} // "some\n"

	n2, err := f.Write(d2)
	check(err)

	fmt.Printf("wrote %d bytes\n", n2)

	// 3. WRITE STRING
	fmt.Println("\n===== WRITE STRING =====")

	n3, err := f.WriteString("writes\n")
	check(err)

	fmt.Printf("wrote %d bytes\n", n3)

	// 4. FORCE WRITE TO DISK (SYNC)
	fmt.Println("\n===== SYNC TO DISK =====")

	err = f.Sync()
	check(err)

	fmt.Println("data synced to disk")

	// 5. BUFFERED WRITING (HIGH PERFORMANCE)
	fmt.Println("\n===== BUFFERED WRITER =====")

	writer := bufio.NewWriter(f)

	n4, err := writer.WriteString("buffered write\n")
	check(err)

	fmt.Printf("buffer wrote %d bytes\n", n4)

	// MUST flush buffered data
	writer.Flush()

	fmt.Println("buffer flushed")

	// 6. APPEND MODE (REAL WORLD LOGGING)
	fmt.Println("\n===== APPEND MODE =====")

	path3 := filepath.Join(os.TempDir(), "log.txt")

	file, err := os.OpenFile(path3, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	check(err)
	defer file.Close()

	_, err = file.WriteString("log entry 1\n")
	check(err)

	_, err = file.WriteString("log entry 2\n")
	check(err)

	fmt.Println("logs appended:", path3)

	// 7. FAST LOGGING USING BUFFER
	fmt.Println("\n===== BUFFERED LOGGING =====")

	bufWriter := bufio.NewWriter(file)

	for i := 1; i <= 3; i++ {
		_, err := bufWriter.WriteString(fmt.Sprintf("buffer log %d\n", i))
		check(err)
	}

	bufWriter.Flush()

	fmt.Println("buffered logs written")

	// 8. REAL WORLD: CSV STYLE EXPORT
	fmt.Println("\n===== CSV EXPORT =====")

	path4 := filepath.Join(os.TempDir(), "data.csv")

	csvFile, err := os.Create(path4)
	check(err)
	defer csvFile.Close()

	csvFile.WriteString("id,name,age\n")
	csvFile.WriteString("1,Alice,25\n")
	csvFile.WriteString("2,Bob,30\n")

	fmt.Println("CSV written:", path4)

	// 9. DIFFERENCE SUMMARY
	fmt.Println("\n===== SUMMARY =====")

	fmt.Println("os.WriteFile  -> simple overwrite")
	fmt.Println("os.Create     -> manual control")
	fmt.Println("bufio.Writer  -> high performance")
	fmt.Println("Sync          -> force disk flush")
	fmt.Println("O_APPEND      -> append mode")
}