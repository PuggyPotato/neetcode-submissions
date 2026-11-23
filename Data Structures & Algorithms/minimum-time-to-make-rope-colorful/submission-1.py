class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        r = 1
        total = 0
        while r < len(colors):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    total += neededTime[l]
                    l = r
                else:
                    total += neededTime[r]
            else:
                l = r
            r += 1
        return total
