func topKFrequent(nums []int, k int) []int {
	result := make([]int,0,k)
	hashMap := make(map[int]int)
	for _, val := range nums {
		hashMap[val]++
	}

	for i:=0; i<k; i++ {
		maxThing := 0
		elementMax := 0
		for element, value := range hashMap {
			if value > maxThing {
				maxThing = value
				elementMax = element
			}
		}
		result = append(result,elementMax)
		hashMap[elementMax] = 0
	}
	return result
}
