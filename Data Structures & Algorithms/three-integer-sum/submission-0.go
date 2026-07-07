import "slices"
func threeSum(nums []int) [][]int {
	slices.Sort(nums)
	result := make([][]int,0)
	for i, val := range nums {
		if val > 0 {
			break
		}

		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		left, right := i + 1, len(nums) - 1

		for left < right {
			total := nums[left] + nums[i] + nums[right]

			if total < 0 {
				left++
			} else if total > 0 {
				right--
			} else {
				result = append(result, []int{nums[i],nums[left],nums[right]})
				left++
				right--
				for left < right && nums[left] == nums[left-1] {
					left++
				}
			}
		}
	}
	return result
}
