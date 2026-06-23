func maxProfit(prices []int) int {
	totalRevenue := 0
	for i:=1;i<len(prices);i++ {
		currProfit := prices[i] - prices[i-1]
		if currProfit > 0 {
			totalRevenue += currProfit
		}
	}
	return totalRevenue
}
