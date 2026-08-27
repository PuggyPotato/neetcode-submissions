class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_count = 0
        count = 1
        ptr = 1
        ascend = False
        descend = True

        if len(nums) < 2:
            return 1

        while ptr < len(nums):

            if ascend and nums[ptr] - nums[ptr - 1] > 0:
                ascend = True
                descend = False
                count += 1
                ptr += 1

            elif descend and nums[ptr] - nums[ptr - 1] < 0:
                descend = True
                ascend = False
                count += 1
                ptr += 1

            elif ascend and nums[ptr] - nums[ptr - 1] < 0:
                ascend = False
                descend = True
                count = 1
            
            elif descend and nums[ptr] - nums[ptr - 1] > 0:
                descend = False
                ascend = True
                count = 1
            
            else:
                count = 1
                ptr += 1

            max_count = max(max_count, count)

            

        return max_count
    