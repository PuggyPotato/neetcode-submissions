func findDuplicate(nums []int) int {
    frequencyMap := make([]int,len(nums)+1)
	for _, val := range nums {
		frequencyMap[val]++
	}

	for i, val := range frequencyMap {
		if val > 1 {
			return i
		}
	} 

	return -1

}
