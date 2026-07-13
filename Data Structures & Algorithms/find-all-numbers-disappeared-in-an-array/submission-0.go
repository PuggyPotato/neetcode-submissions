func findDisappearedNumbers(nums []int) []int {
	seenMap := make(map[int]struct{})
	result := make([]int,0)

	for _,val := range nums {
		seenMap[val] = struct{}{}
	}

	for i := 1; i <= len(nums); i++{
		if _,ok := seenMap[i]; !ok {
			result = append(result,i)
		}
	}

	return result
}
