class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        low1 = 101
        low2 = 101

        for i in range(len(prices)):
            if prices[i] < low1:
                low2,low1 = low1, low2
                low1 = prices[i]
            elif prices[i] < low2:
                low2 = prices[i]

        total = money - low1 - low2

        if total >= 0:
            return total

        return money