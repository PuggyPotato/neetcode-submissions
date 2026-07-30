class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        result1 = []
        result2 = []

        for val in set1:
            if val not in set2:
                result1.append(val)

        for val in set2:
            if val not in set1:
                result2.append(val)

        return [result1,result2]