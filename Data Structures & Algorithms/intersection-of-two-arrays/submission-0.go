func intersection(nums1 []int, nums2 []int) []int {
    seen := make(map[int]bool)
	result := make([]int,0)
	for _, val := range nums1 {
		seen[val] = true
	}

	for _, val := range nums2 {
		if seen[val] {
			result = append(result,val)
		}
		seen[val] = false
	}
	return result
}
