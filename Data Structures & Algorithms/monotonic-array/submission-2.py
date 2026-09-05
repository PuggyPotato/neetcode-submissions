class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        isIncrease = 2
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1] and (isIncrease == 2 or isIncrease == 1):
                isIncrease = 1
            elif nums[i] < nums[i - 1] and (isIncrease == 2 or isIncrease == 0):
                isIncrease = 0
            elif nums[i] == nums[i - 1]:
                pass
            else:
                return False

        return True