class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for i in range(len(nums)):
            count += nums[i]

        for i in range(len(nums) + 1):
            total += i

        return total - count