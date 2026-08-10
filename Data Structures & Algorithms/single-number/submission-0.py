class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0
        for val in nums:
            count ^= val

        return count