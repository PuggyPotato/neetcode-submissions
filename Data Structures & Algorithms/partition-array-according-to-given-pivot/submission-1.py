from collections import deque
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []

        for val in nums:
            if val < pivot:
                result.append(val)

        for val in nums:
            if val == pivot:
                result.append(val)

        for val in nums:
            if val > pivot:
                result.append(val)

        return result