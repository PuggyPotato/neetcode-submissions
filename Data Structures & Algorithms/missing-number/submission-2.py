class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = len(nums)
        for i,val in enumerate(nums):
            start ^= val ^ i

        return start