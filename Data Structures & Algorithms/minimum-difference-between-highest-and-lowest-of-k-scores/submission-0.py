class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        min_diff = float('inf')

        for i in range(len(nums) - k + 1):
            current = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, current)


        return min_diff