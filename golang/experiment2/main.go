package main

import "fmt"

func sumDigits(n int) int {
	totalSum := 0
	for n > 0 {
		digit := n % 10
		n = n / 10
		totalSum += digit * digit
	}

	return totalSum
}

func is_happy(n int) bool {
	sp := n
	fp := sumDigits(n)

	for fp != 1 && sp != fp {
		sp = sumDigits(sp)
		fp = sumDigits(sumDigits(fp))
	}

	if fp == 1 {
		return true
	}

	return false

}

func main() {
	fmt.Println("Hello, 世界")

	tc := []int{1, 4, 7, 13, 20, 23, 28, 30}

	for _, v := range tc {
		fmt.Println(v, " : ", is_happy(v))
	}
}
