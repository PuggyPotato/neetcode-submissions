func sortArrayByParity(nums []int) []int {
	left := 0
	right := len(nums) - 1
	for left < right {
		if nums[left] % 2 == 0 {
			left++
		} else if nums[left] % 2 != 0 {
			nums[left],nums[right] = nums[right], nums[left]
			right--
		}
	}
	return nums
}
