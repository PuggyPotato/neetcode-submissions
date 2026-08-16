class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for val in nums2:
            while stack and val > stack[-1]:
                smaller_num = stack.pop()
                next_greater[smaller_num] = val

            stack.append(val)

        result = []
        for num in nums1:
            result.append(next_greater.get(num, -1))

        return result