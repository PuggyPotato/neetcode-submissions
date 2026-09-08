class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        duplicate = -1

        for val in nums:
            index = abs(val) - 1
            if nums[index] < 0:
                duplicate = abs(val)
                break

            nums[index] = -nums[index]

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1

        sum_total = sum(nums) - duplicate

        for i in range(len(nums) + 1):
            sum_total -= i

        return [duplicate, -sum_total]
