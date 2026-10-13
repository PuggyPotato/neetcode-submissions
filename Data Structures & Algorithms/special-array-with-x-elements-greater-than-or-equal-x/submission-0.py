class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        

        for i in range(len(nums)):
            count = i + 1

            if nums[i] >= count:
                if count == len(nums) or nums[count] < count:
                    return count

        return -1