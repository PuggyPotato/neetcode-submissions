func containsNearbyDuplicate(nums []int, k int) bool {
	leftPtr := 0
	rightPtr := 1
	for rightPtr < len(nums) {
		if nums[leftPtr] == nums[rightPtr] {
			absVal := leftPtr - rightPtr
			if absVal < 0 {
				absVal = -absVal
			}
			if absVal <= k {
				return true
			}
		}
		rightPtr++
		if rightPtr == len(nums){
			leftPtr++
			rightPtr = leftPtr + 1
		}
	}
	return false
}
