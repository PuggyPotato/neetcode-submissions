class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l,e,g = [], [], []

        for val in nums:
            if val < pivot:
                l.append(val)
            elif val == pivot:
                e.append(val)
            else:
                g.append(val)

        return l + e + g