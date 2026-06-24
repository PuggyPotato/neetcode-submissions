func sortArray(nums []int) []int {
	return mergeSort(nums)
}

func mergeSort(items []int) []int{
	if len(items) <= 1 {
		return items
	}
	mid := len(items) / 2

	left := mergeSort(items[:mid])
	right := mergeSort(items[mid:])

	return merge(left,right)
}

func merge(left []int, right []int) []int{
	result := make([]int,0)
	i := 0
	j := 0
	for i < len(left) && j < len(right) {
		if left[i] > right[j] {
			result = append(result,right[j])
			j++
		} else {
			result = append(result,left[i])
			i++
		}
	}
	result = append(result, left[i:]...)
	result = append(result, right[j:]...)

	return result
}
