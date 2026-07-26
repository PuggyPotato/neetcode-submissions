class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = len(heights)
        sorted_array = sorted(heights)
        for i in range(len(heights)):
            if sorted_array[i] == heights[i]:
                count -= 1

        return count