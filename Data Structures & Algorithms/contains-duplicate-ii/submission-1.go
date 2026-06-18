func containsNearbyDuplicate(nums []int, k int) bool {
	seen := make(map[int]int)
	for i, val := range nums {
		if j,ok := seen[val]; ok {
			absVal := j - i
			if absVal < 0 {
				absVal = -absVal
			} 
			if absVal <= k {
				return true
			}
		}
		seen[val] = i
	}
	return false
}
