import "slices"
func numRescueBoats(people []int, limit int) int {
	slices.Sort(people)
	left := 0
	right := len(people) - 1
	count := 0
	for left <= right {
		if people[left] + people[right] <= limit {
			count++
			left++
		} else {
			count++
		}
		right--
	}
	return count
}
