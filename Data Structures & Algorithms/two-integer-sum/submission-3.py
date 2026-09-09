class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}

        for i, val in enumerate(nums):

            complement = target - val

            if complement in hp:
                return [hp[complement], i]

            hp[val] = i

        return [-1,-1] 