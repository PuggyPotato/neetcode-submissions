class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                target = nums[l] + nums[i] + nums[r]
                if target == 0:
                    result.append([nums[l], nums[i], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif target < 0:
                    l += 1
                else:
                    r -= 1

        return result
