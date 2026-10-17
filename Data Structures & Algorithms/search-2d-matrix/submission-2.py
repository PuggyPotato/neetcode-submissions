class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        targetm = -1

        for i,n in enumerate(matrix):
            if n[-1] >= target:
                targetm = i
                break

        array = matrix[targetm]

        l = 0
        r = len(array) - 1

        while l <= r:
            mid = (l + r) // 2
            if array[mid] == target:
                return True
            elif array[mid] > target:
                r = mid - 1
            else:
                l = mid + 1


        return False