class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        #print(len(grid) * len(grid[0]))
        array_value = [0] * (len(grid) * len(grid[0]) + 1) 
        for array in grid:
            for value in array:
                array_value[value] += 1

        result = [0] * 2
        for i,val in enumerate(array_value):
            if val == 0:
                result[1] = i
            elif val == 2:
                result[0] = i

        return result