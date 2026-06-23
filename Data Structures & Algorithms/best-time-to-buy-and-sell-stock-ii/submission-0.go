func maxProfit(prices []int) int {
	currRevenue := 0
	for i:=1;i<len(prices);i++ {
		if prices[i] - prices[i-1] > 0 {
			currRevenue += prices[i] - prices[i-1]
		}
	}
	return currRevenue
}
