func rotate(nums []int, k int) {
	for i :=0;i < k;i++ {
		for j :=1;j<len(nums);j++ {
			nums[0],nums[j] = nums[j], nums[0]
		}
	}
}
