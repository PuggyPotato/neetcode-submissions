func intersection(nums1 []int, nums2 []int) []int {
    seen := make(map[int]struct{},len(nums1))
	result := make([]int,0)
	for _, val := range nums1 {
		seen[val] = struct{}{}
	}

	for _, val := range nums2 {
		if _,ok := seen[val]; ok  {
			result = append(result,val)
			delete(seen,val)
		}
	}
	return result
}
