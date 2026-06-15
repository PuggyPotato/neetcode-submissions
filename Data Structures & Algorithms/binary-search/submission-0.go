func search(nums []int, target int) int {
	for i,value := range nums {
		if value == target {
			return i
		}
	}
	return -1
}
