
func maxProductDifference(nums []int) int {
	max1,max2,min1,min2 := -99999999,-99999999,99999999,99999999

	for _, val := range nums {

		if val > max1 {
			max1,max2 = val,max1
		} else if val > max2 {
			max2 = val
		}

		if val < min1 {
			min1,min2 = val,min1
		} else if val < min2 {
			min2 = val
		}

	}
	return max1 * max2 - min1 * min2
}