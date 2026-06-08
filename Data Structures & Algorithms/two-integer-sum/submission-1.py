class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        notebook = {}
        for i in  range(len(nums)):
            complement = target - nums[i]
            if complement in notebook:
                return [notebook[complement],i]
            notebook[nums[i]] = i
        