class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left,right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            is_even = (mid % 2 == 0)

            if is_even:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid

        return nums[left] 