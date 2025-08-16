package main

import "fmt"

func main() {
	sum := sum(10, 5)
	sub := sub(10, 5)
	mult := mult(10, 5)
	divi := divi(10, 5)
	
	fmt.Println(sum)
	fmt.Println(sub)
	fmt.Println(mult)
	fmt.Println(divi)
}

func sum(num1, num2 int) int {
	return num1 + num2
}

func sub(num1, num2 int) int {
	return num1 - num2
}

func mult(num1, num2 int) int {
	return num1 * num2
}

func divi(num1, num2 float64) float64 {
	return num1 / num2
}