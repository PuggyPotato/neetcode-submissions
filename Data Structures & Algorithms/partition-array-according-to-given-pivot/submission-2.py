from collections import deque
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []
        count = 0

        for val in nums:
            if val < pivot:
                result.append(val)
            if val == pivot:
                count += 1
        
        result += [pivot] * count

        for val in nums:
            if val > pivot:
                result.append(val)

        return result