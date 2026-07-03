func rotate(nums []int, k int) {
	for i :=0;i < k;i++ {
		for i :=1;i<len(nums);i++ {
			nums[0],nums[i] = nums[i], nums[0]
		}
	}
}
