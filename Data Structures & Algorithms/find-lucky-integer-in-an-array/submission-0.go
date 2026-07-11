func findLucky(arr []int) int {
	currentLuckiest := -1
	freq := make(map[int]int)

	for _, val := range arr {
		freq[val]++
	}

	for key,val := range freq {
		if key == val && key > currentLuckiest {
			currentLuckiest = key
		}
	}
	return currentLuckiest
}
