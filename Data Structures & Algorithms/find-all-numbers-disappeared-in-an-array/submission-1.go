func findDisappearedNumbers(nums []int) []int {
	freqMap := make([]int,100001)
	result := make([]int,0)

	for _,val := range nums {
		freqMap[val]++
	}

	for i := 1; i <= len(nums); i++{
		if freqMap[i] == 0 {
			result = append(result, i)
		}
	}

	return result
}
