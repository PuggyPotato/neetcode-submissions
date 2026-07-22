func divideArray(nums []int) bool {
    seen := make(map[int]int)
	for _, val := range nums {
		seen[val]++
	}

	for _,val := range seen {
		if val % 2 != 0 {
			return false
		}
	}
	
	return true
}