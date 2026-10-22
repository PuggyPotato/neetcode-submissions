class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []

        if len(original) != (m * n):
            return []

        num_per_row = len(original) // m

        temp = []
        
        for i, val in enumerate(original):

            if i % num_per_row == 0 and i != 0:
                result.append(temp)
                temp = []

            temp.append(val)

            if i == len(original) - 1:
                result.append(temp)

        return result