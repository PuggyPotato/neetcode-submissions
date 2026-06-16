func findMaxConsecutiveOnes(nums []int) int {
	max := 0
	tempMax := 0
	for _,val := range nums {
		if val == 1 {
			tempMax +=1
		} else {
			tempMax = 0
		}
		if tempMax > max {
			max = tempMax
		}
	}
	return max
}
