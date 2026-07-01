func firstMissingPositive(nums []int) int {
	freq := make([]int,100001)
	min := 999999999999999
	for _, val := range nums {
		if val > 0 {
			if val < min {
				min = val
			}
			freq[val]++
		}
	}

	for i := 1; i < 100001;i++ {
		print(i)
		if freq[i] == 0 {
			return i
		}
	}
	return 1
}
