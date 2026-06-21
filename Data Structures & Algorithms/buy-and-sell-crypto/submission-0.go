func maxProfit(prices []int) int {
	minNum := prices[0]
	maxPrice := 0
	for _, val := range prices {
		if val - minNum > maxPrice {
			maxPrice = val-minNum
		}
		if val < minNum {
			minNum = val
		}
	}
	return maxPrice
}
