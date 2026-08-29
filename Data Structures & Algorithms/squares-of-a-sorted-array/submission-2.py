class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        left = 0
        right = length - 1
        
        for i in range(length - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
                
        return result