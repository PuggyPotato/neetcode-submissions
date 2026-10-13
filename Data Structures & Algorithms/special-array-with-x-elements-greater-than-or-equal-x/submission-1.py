class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        n = len(nums)

        counts = [0] * (n + 1)

        for num in nums:
            if num >= n:
                counts[n] += 1
            else:
                counts[num] += 1

        total = 0

        for i in range(n, -1, -1):
            total += counts[i]

            if total == i:
                return i

        return -1