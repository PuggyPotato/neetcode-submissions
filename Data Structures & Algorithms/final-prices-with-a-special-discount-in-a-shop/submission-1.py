class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, val in enumerate(prices):
            while stack and val <= prices[stack[-1]]:
                prices[stack[-1]] = prices[stack[-1]] - val
                stack.pop()
            stack.append(i)

        return prices
