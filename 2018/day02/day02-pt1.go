package main

import (
	"fmt"
	"io/ioutil"
	"path/filepath"
	"strings"
)

func getInput() []string {
	filename, err := filepath.Abs("input.txt")
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	idArray := strings.Split(string(data), "\n")

	return idArray
}

func inMap(num int, array map[string]int) bool {
	// inSlice checks to see if a value matches
	// and item in a slice.
	for _, value := range array {
		if num == value {
			return true
		}
	}

	return false
}

func countChars(id string) map[string]int {
	// countChars makes a map of the number of
	// the same like characters in each string
	count := make(map[string]int)

	for _, char := range id {
		char := string(char)

		if _, ok := count[char]; ok {
			count[char]++
		} else {
			count[char] = 1
		}
	}

	return count
}

// Main function
func main() {
	data := getInput()
	twoCount := 0
	threeCount := 0

	for _, id := range data {
		charCount := countChars(id)

		if inMap(2, charCount) {
			twoCount++
		}

		if inMap(3, charCount) {
			threeCount++
		}
	}

	fmt.Printf("The checksum is: %d\n", twoCount*threeCount)

}
