class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []

        l = 0
        r = 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l][0] == nums2[r][0]:
                result.append([nums1[l][0], nums1[l][1] + nums2[r][1]])
                l += 1
                r += 1
            elif nums1[l][0] < nums2[r][0]:
                result.append([nums1[l][0], nums1[l][1]])
                l += 1
            else:
                result.append([nums2[r][0], nums2[r][1]])
                r += 1
        
        result.extend(nums1[l:])
        result.extend(nums2[r:])

        return result

        

