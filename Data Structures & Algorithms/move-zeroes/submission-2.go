func moveZeroes(nums []int) {
	leftPtr := 0

	for leftPtr < len(nums) && nums[leftPtr] != 0 {
		leftPtr++
	}
	rightPtr := leftPtr + 1

	for rightPtr < len(nums) {
		if nums[rightPtr] != 0 {
			nums[leftPtr], nums[rightPtr] = nums[rightPtr], nums[leftPtr]
			leftPtr++
		}
		rightPtr++
	}
}
