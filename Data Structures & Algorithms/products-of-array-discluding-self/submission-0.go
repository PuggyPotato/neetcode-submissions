func productExceptSelf(nums []int) []int {
	arr := make([]int,len(nums))
	for i,_ := range nums {
		arr[i] = 1
		for j,_ := range nums {
			if i != j {
				arr[i] *= nums[j]
			}
		}
	}
	return arr
}
