class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *=2
                nums[i + 1] = 0
        
        x = 0
        count = 0
        for val in nums:
            if val != 0:
                nums[x] = val
                x += 1
            else:
                count += 1

        for i in range(len(nums) -1, len(nums) - count - 1, -1):
            nums[i] = 0
        
        return nums