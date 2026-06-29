func maxArea(heights []int) int {
	left := 0
	right := len(heights) - 1
	maxArea := 0
	for left < right {
		minHeight := 0
		if heights[left] > heights[right] {
			minHeight = heights[right]
		} else{
			minHeight = heights[left]
		}
		width := right - left
		currArea := width * minHeight
		if currArea > maxArea {
			maxArea = currArea
		}

		if heights[left] > heights[right] {
			right--
		} else{
			left++
		}
	}
	return maxArea
}
