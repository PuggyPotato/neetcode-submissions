func sortColors(nums []int) {
	if len(nums) < 2 {
		return
	}
	if len(nums) < 3 {
		if nums[0] > nums[1] {
			nums[1], nums[0] = nums[0], nums[1]
		}
		return
	}

	low := 0
	mid := 0
	high := len(nums) - 1

	for mid <= high {
		switch nums[mid] {
			case 0:
				nums[low], nums[mid] = nums[mid], nums[low]
				mid++
				low++
			case 1:
				mid++
			case 2:
				nums[high], nums[mid] = nums[mid], nums[high]
				high--
		}
	}
}
