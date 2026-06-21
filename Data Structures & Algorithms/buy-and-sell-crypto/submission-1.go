func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}

	minNum := prices[0]
	maxProfit := 0

	for _, val := range prices {
		if val - minNum > maxProfit {
			maxProfit = val-minNum
		}
		if val < minNum {
			minNum = val
		}
	}
	return maxProfit
}
