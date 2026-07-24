func sortPeople(names []string, heights []int) []string {
	for i := 0;i<len(heights);i++ {
		for j:=i; j > 0 && heights[j-1] < heights[j]; j-- {
			heights[j], heights[j-1] = heights[j-1], heights[j]
			names[j], names[j-1] = names[j-1], names[j]
		}
	}
	return names
}