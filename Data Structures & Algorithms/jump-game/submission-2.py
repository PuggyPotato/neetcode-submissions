class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if max_reach < i:
                return False
            max_reach = max(max_reach, i + jump)
        
        return True