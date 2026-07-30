class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        result1 = []
        result2 = []

        for i in range(len(nums1)):
            if nums1[i] not in set2 and nums1[i] not in result1:
                result1.append(nums1[i])
            
        for i in range(len(nums2)):
            if nums2[i] not in set1 and nums2[i] not in result2:
                result2.append(nums2[i])

        result = []
        result.append(result1)
        result.append(result2)
        return result