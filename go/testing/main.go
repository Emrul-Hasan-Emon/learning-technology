package mathutils

import (
	"errors"
	"fmt"
	"os"
	"testing"
)

//////////////////////
// CODE UNDER TEST  //
//////////////////////

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func Divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("divide by zero")
	}
	return a / b, nil
}

func Fibonacci(n int) int {
	if n < 0 {
		panic("negative number not allowed")
	}
	if n <= 1 {
		return n
	}
	return Fibonacci(n-1) + Fibonacci(n-2)
}

func IsPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

/////////////////////////
// TEST SETUP/TEARDOWN //
/////////////////////////

func TestMain(m *testing.M) {
	fmt.Println("🔧 Setup before tests")
	code := m.Run()
	fmt.Println("🧹 Teardown after tests")
	os.Exit(code)
}

//////////////////////
// BASIC UNIT TESTS //
//////////////////////

func TestMinBasic(t *testing.T) {
	ans := Min(10, 5)
	if ans != 5 {
		t.Errorf("expected 5 got %d", ans)
	}
}

func TestMaxBasic(t *testing.T) {
	ans := Max(10, 5)
	if ans != 10 {
		t.Errorf("expected 10 got %d", ans)
	}
}

/////////////////////////////
// TABLE DRIVEN TESTS      //
/////////////////////////////

func TestMinTableDriven(t *testing.T) {
	tests := []struct {
		a, b, want int
	}{
		{1, 2, 1},
		{2, 1, 1},
		{-1, -5, -5},
		{0, 0, 0},
	}

	for _, tt := range tests {
		name := fmt.Sprintf("%d,%d", tt.a, tt.b)

		t.Run(name, func(t *testing.T) {
			got := Min(tt.a, tt.b)
			if got != tt.want {
				t.Fatalf("got %d want %d", got, tt.want)
			}
		})
	}
}

//////////////////////
// ERROR TESTING    //
//////////////////////

func TestDivide_Error(t *testing.T) {
	_, err := Divide(10, 0)
	if err == nil {
		t.Fatal("expected divide by zero error")
	}
}

func TestDivide_Success(t *testing.T) {
	ans, err := Divide(10, 2)
	if err != nil {
		t.Fatal(err)
	}
	if ans != 5 {
		t.Fatalf("expected 5 got %d", ans)
	}
}

//////////////////////
// PANIC TESTING    //
//////////////////////

func TestFibonacci_Panic(t *testing.T) {
	defer func() {
		if r := recover(); r == nil {
			t.Errorf("expected panic")
		}
	}()
	Fibonacci(-1)
}

//////////////////////
// EDGE CASE TESTS  //
//////////////////////

func TestIsPrime_EdgeCases(t *testing.T) {
	tests := map[int]bool{
		-1: false,
		0:  false,
		1:  false,
		2:  true,
		3:  true,
		4:  false,
	}

	for input, want := range tests {
		got := IsPrime(input)
		if got != want {
			t.Errorf("IsPrime(%d) = %v, want %v", input, got, want)
		}
	}
}

//////////////////////
// PARALLEL TESTS   //
//////////////////////

func TestParallelMin(t *testing.T) {
	tests := []struct{ a, b int }{
		{1, 2}, {10, 5}, {-1, -5},
	}

	for _, tt := range tests {
		tt := tt
		t.Run("parallel", func(t *testing.T) {
			t.Parallel()
			Min(tt.a, tt.b)
		})
	}
}

//////////////////////
// SKIP TEST        //
//////////////////////

func TestSkipShortMode(t *testing.T) {
	if testing.Short() {
		t.Skip("Skipping slow test in short mode")
	}
	Fibonacci(35)
}

/////////////////////////////
// EXAMPLE (DOC) TESTS     //
/////////////////////////////

func ExampleMin() {
	fmt.Println(Min(3, 5))
	// Output: 3
}

//////////////////////
// BENCHMARKS       //
//////////////////////

// Classic benchmark loop
func BenchmarkMin(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Min(10, 20)
	}
}

// New Go 1.22 benchmark loop
func BenchmarkMinLoop(b *testing.B) {
	for b.Loop() {
		Min(10, 20)
	}
}

// Table driven benchmark
func BenchmarkFibonacci(b *testing.B) {
	tests := []int{5, 10, 15}

	for _, n := range tests {
		b.Run(fmt.Sprintf("Fib(%d)", n), func(b *testing.B) {
			for b.Loop() {
				Fibonacci(n)
			}
		})
	}
}

// Memory allocation benchmark
func BenchmarkPrimeMemory(b *testing.B) {
	b.ReportAllocs()
	for b.Loop() {
		IsPrime(104729)
	}
}