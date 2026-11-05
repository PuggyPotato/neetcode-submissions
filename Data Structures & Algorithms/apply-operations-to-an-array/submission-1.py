class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *=2
                nums[i + 1] = 0
        result = [0] * len(nums) 
        x = 0
        for val in nums:
            if val != 0:
                result[x] = val
                x += 1
        
        return result