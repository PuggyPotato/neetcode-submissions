class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        num = nums[0]
        isIncrease = 2
        for i in range(1,len(nums)):
            if nums[i] > num and (isIncrease == 2 or isIncrease == 1):
                isIncrease = 1
            elif nums[i] < num and (isIncrease == 2 or isIncrease == 0):
                isIncrease = 0
            elif nums[i] == num:
                pass
            else:
                return False

            num = nums[i]
            

        return True