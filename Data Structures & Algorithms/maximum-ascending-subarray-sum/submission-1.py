class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp += nums[i]
            else:
                temp = nums[i]
            
            max_sum = max(max_sum, temp)


        return max_sum