class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 1

        increment_count = 1
        decrement_count = 1
        max_count = 0
        for i in range(1, len(nums)):

            if nums[i] - nums[i - 1] > 0:
                increment_count += 1
                decrement_count = 1
            elif nums[i] - nums[i - 1] < 0:
                decrement_count += 1
                increment_count = 1
            else:
                increment_count = 1
                decrement_count = 1

            max_count = max(max_count, increment_count, decrement_count)

        return max_count