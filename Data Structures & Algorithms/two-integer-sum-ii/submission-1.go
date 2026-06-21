func twoSum(numbers []int, target int) []int {
	leftPtr := 0
	rightPtr := len(numbers) - 1
	for leftPtr < rightPtr{
		currentSum := numbers[leftPtr] + numbers[rightPtr] 
		if currentSum < target {
			leftPtr++
		} else if currentSum > target {
			rightPtr--
		} else {
			return []int{leftPtr +1, rightPtr +1}
		}
	}
	return nil
}
