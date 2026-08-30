class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        freq = [0] * 20000
        count = 0

        for i in range(len(nums)):
            freq[nums[i]] += 1
            if freq[nums[i]] > 2:
                nums[i] = 9999999
            else:
                count += 1

        nums.sort()

        return count