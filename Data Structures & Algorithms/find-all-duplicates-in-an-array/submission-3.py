class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for i, val in enumerate(nums):
            val = abs(val)
            if nums[val - 1] < 0:
                result.append(val)
 

            nums[val - 1] = -nums[val - 1]


        return result