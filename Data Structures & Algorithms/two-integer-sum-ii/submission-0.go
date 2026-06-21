func twoSum(numbers []int, target int) []int {
	leftPtr := 0
	rightPtr := len(numbers) - 1
	for {
		if numbers[leftPtr] + numbers[rightPtr] < target {
			leftPtr++
		} else if numbers[leftPtr] + numbers[rightPtr] > target {
			rightPtr--
		} else {
			return []int{leftPtr +1, rightPtr +1}
		}
	}
}
