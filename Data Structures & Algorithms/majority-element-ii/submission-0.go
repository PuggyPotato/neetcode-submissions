func majorityElement(nums []int) []int {
	n := len(nums) / 3
	result := make([]int,0,len(nums))
	seenMap := make(map[int]int)
	for _, val := range nums {
		seenMap[val]++
	}

	for key,value := range seenMap {
		if value > n {
			result = append(result,key)
		}
	}
	return result
}
