package main

import "fmt"

func main() {
	fmt.Println("Hello World!")

	var name string
	var age int

	name = "Mauricio"
	age = 19

	fmt.Printf("Name: %s, age: %d\n", name, age)

	if age > 18 {
		fmt.Println("Adult")
	} else {
		fmt.Println("Child/Teen")
	}

	x := 10
	for i := 1; i <= 10; i++ {
		var a int = x * i
		fmt.Printf("%d x %d = %d\n", x, i, a)
	}

	// Array: tamanha definido
	// Slices: sem tamanho definido
	fruits := [3]string{"Banana", "Apple", "Berry"} // Array
	cars := []string{"BMW", "Ferrari", "Mercedes"} // Slice

	for _, fruit := range fruits {
		fmt.Printf("Fruit: %s\n", fruit)
	}

	for _, car := range cars {
		fmt.Printf("Car: %s\n", car)
	}
}