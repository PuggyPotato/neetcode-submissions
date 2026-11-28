class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        total = 0

        for i, num in enumerate(nums):
            key = num - i
            total += i - freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        return total