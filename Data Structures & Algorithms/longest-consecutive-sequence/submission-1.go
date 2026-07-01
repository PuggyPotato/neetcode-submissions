import "slices"
func longestConsecutive(nums []int) int {
	slices.Sort(nums)
	temp := 0
	result := 0
	if len(nums) < 1 {
		return 0
	}
	for i:=0;i<len(nums)-1;i++{
		if nums[i] + 1 == nums[i+1] {
			temp++
			if temp > result {
				result = temp
			}
		} else if nums[i] == nums[i+1] {

		} else {
			temp = 0
		}
	}
	return result + 1
}
