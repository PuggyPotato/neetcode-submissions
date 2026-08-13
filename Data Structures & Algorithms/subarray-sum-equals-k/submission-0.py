class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        earlier_sum = 0
        seen_sum = {0:1}

        for val in nums:
            current_sum += val
            earlier_sum = current_sum - k
            if earlier_sum in seen_sum:
                count += seen_sum[earlier_sum]
            seen_sum[current_sum] = seen_sum.get(current_sum, 0) + 1

        return count