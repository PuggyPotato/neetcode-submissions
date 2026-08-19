class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_elements = n * n
        freq = [0] * (total_elements + 1)
        missing_value = 0
        repeated_value = 0
        
        for row in grid:
            for val in row:
                freq[val] += 1

        for i in range(1, total_elements + 1):
            if freq[i] == 2:
                repeated_value = i
            elif freq[i] == 0:
                missing_value = i
        return [repeated_value, missing_value]