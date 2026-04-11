package main

import (
	"fmt"
	"math/rand/v2"
)

func main() {

	// ------------------------------------------------------------
	// 1️. BASIC RANDOM INTEGERS
	// ------------------------------------------------------------
	fmt.Println("===== BASIC RANDOM INTS =====")

	fmt.Println("Random 0-99:", rand.IntN(100))
	fmt.Println("Random 0-99:", rand.IntN(100))

	// ------------------------------------------------------------
	// 2️. RANDOM FLOATS
	// ------------------------------------------------------------
	fmt.Println("\n===== RANDOM FLOATS =====")

	fmt.Println("Float 0-1:", rand.Float64())

	// scale float to range (5 to 10)
	fmt.Println("Float 5-10:", (rand.Float64()*5)+5)

	// ------------------------------------------------------------
	// 3️. RANDOM BOOL (SIMULATION USE CASE)
	// ------------------------------------------------------------
	fmt.Println("\n===== RANDOM BOOL =====")

	fmt.Println("Coin flip:", rand.IntN(2) == 0)

	// ------------------------------------------------------------
	// 4️. SEEDLESS RANDOM (NON-DETERMINISTIC)
	// ------------------------------------------------------------
	fmt.Println("\n===== SEEDLESS RANDOM =====")

	fmt.Println(rand.IntN(100))
	fmt.Println(rand.IntN(100))
	fmt.Println(rand.IntN(100))

	// ------------------------------------------------------------
	// 5️. SEEDED RANDOM (DETERMINISTIC OUTPUT)
	// ------------------------------------------------------------
	fmt.Println("\n===== SEEDED RANDOM =====")

	// PCG seed generator (important for reproducibility)
	s1 := rand.NewPCG(42, 1024)
	r1 := rand.New(s1)

	fmt.Print(r1.IntN(100), ", ")
	fmt.Print(r1.IntN(100), ", ")
	fmt.Println(r1.IntN(100))

	// Same seed = same output (VERY IMPORTANT)
	s2 := rand.NewPCG(42, 1024)
	r2 := rand.New(s2)

	fmt.Print(r2.IntN(100), ", ")
	fmt.Print(r2.IntN(100), ", ")
	fmt.Println(r2.IntN(100))

	// ------------------------------------------------------------
	// 6️. RANDOM RANGE GENERATION
	// ------------------------------------------------------------
	fmt.Println("\n===== RANGE GENERATION =====")

	min := 50
	max := 100

	randomInRange := min + rand.IntN(max-min)
	fmt.Println("Random 50-100:", randomInRange)

	// ------------------------------------------------------------
	// 7️. RANDOM ARRAY SELECTION
	// ------------------------------------------------------------
	fmt.Println("\n===== RANDOM SELECTION =====")

	colors := []string{"red", "green", "blue", "yellow"}

	randomIndex := rand.IntN(len(colors))
	fmt.Println("Random color:", colors[randomIndex])

	// ------------------------------------------------------------
	// 8️. SHUFFLE SLICE (VERY COMMON)
	// ------------------------------------------------------------
	fmt.Println("\n===== SHUFFLE =====")

	numbers := []int{1, 2, 3, 4, 5}

	rand.Shuffle(len(numbers), func(i, j int) {
		numbers[i], numbers[j] = numbers[j], numbers[i]
	})

	fmt.Println("Shuffled:", numbers)

	// ------------------------------------------------------------
	// 9️. REAL WORLD: MOCK DATA GENERATION
	// ------------------------------------------------------------
	fmt.Println("\n===== MOCK DATA =====")

	type User struct {
		ID   int
		Age  int
		Name string
	}

	names := []string{"Alice", "Bob", "Charlie", "David"}

	users := make([]User, 3)

	for i := range users {
		users[i] = User{
			ID:   i + 1,
			Age:  18 + rand.IntN(30),
			Name: names[rand.IntN(len(names))],
		}
	}

	fmt.Println(users)

	// ------------------------------------------------------------
	// 10. SIMULATION EXAMPLE (GAME STYLE)
	// ------------------------------------------------------------
	fmt.Println("\n===== GAME SIMULATION =====")

	playerHealth := 100

	for i := 0; i < 5; i++ {
		damage := rand.IntN(20)
		playerHealth -= damage

		fmt.Printf("Turn %d: damage=%d, health=%d\n",
			i+1, damage, playerHealth)
	}
}