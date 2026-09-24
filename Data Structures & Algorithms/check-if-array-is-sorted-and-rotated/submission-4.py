class Solution:
    def check(self, nums: List[int]) -> bool:
        lowest_i = 0
        low = 101
        for i in range(len(nums)):
            if nums[i] < low:
                low = nums[i]
                lowest_i = i


        for i in range(lowest_i, len(nums) -1):
            if nums[i + 1] - nums[i] < 0:
                return False

        for i in range(lowest_i):
            if nums[i] - nums[i - 1] < 0:
                return False

        return True