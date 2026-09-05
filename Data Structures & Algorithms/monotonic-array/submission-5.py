class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        isIncrease = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1] and (isIncrease == 0 or isIncrease == 1):
                isIncrease = 1
            elif nums[i] < nums[i - 1] and (isIncrease == -1 or isIncrease == 0):
                isIncrease = -1
            elif nums[i] == nums[i - 1]:
                pass
            else:
                return False

        return True