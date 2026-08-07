class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set()
        for val in nums:
            seen.add(val)

        for i in range(len(nums)):
            if i not in seen:
                return i

        return len(nums)