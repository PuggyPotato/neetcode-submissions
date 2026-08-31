class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        swap = 2
        if len(nums) <= 2:
            return 0

        for i in range(2, len(nums)):
            if nums[i] != nums[swap - 2]:
                nums[swap] = nums[i]
                swap += 1
        

        return swap