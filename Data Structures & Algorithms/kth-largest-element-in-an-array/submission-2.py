class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [0] * 2001

        for val in nums:
            arr[val + 1000] += 1

        for i in range(len(arr) -1, -1, -1):
            k-= arr[i]
            
            if k <= 0:
                return i - 1000

        return -1