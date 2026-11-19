class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum_water = 0
        r = len(heights) -1 
        l = 0
        while l < r:
            maximum_water = max((min(heights[l], heights[r]) * (r - l)), maximum_water)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maximum_water 