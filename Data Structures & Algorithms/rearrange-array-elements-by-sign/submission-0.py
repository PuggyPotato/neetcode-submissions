class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        ptr1 = 0
        ptr2 = 1

        for val in nums:
            if val > 0:
                result[ptr1] = val
                ptr1 += 2
            else:
                result[ptr2] = val
                ptr2 += 2
        return result

