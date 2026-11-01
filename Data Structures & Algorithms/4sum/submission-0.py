class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        seen = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    total = nums[l] + nums[r] + nums[i] + nums[j]

                    if total == target:
                        if (nums[i], nums[j], nums[l], nums[r]) not in seen:
                            result.append([nums[i], nums[j], nums[l], nums[r]])
                            seen.add((nums[i], nums[j], nums[l], nums[r]))

                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                    elif total > target:
                        r -= 1
                    else:
                        l += 1

        return result