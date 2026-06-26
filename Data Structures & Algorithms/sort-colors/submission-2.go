func sortColors(nums []int) {
	count := [3]int{0,0,0}
	for _, val := range nums {
		count[val]++
	}

	counting := 0
	countIndex := 0

	for _, val := range count {
		for i:=0;i< val;i++ {
			nums[countIndex] = counting
			countIndex++
		}
		counting++
	}
}
