class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for i, val in enumerate(nums):
            
            if nums[abs(val) - 1] < 0:
                result.append(abs(val))
 

            nums[abs(val) - 1] = -nums[abs(val) - 1]


        return result