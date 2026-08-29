class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if (nums[i] * nums[i]) < (nums[-1] * nums[-1]):
                nums[i] *= nums[i]
            else:
                nums[i],nums[-1] = nums[-1], nums[i]
                nums[i] *= nums[i]

        nums.sort()

        return nums
            