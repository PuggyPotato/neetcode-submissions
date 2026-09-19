class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = nums[0]
        for i in range(1,len(nums)):
            count *= nums[i]
            if count == 0:
                return 0

        if count > 0:
            return 1

        return -1