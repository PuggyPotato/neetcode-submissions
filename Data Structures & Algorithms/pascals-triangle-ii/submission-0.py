class Solution:
    def getRow(self, numRows: int) -> List[List[int]]:
        result = [[1],[1,1]]

        if numRows == 0:
            return [1]
        elif numRows == 1:
            return [1,1]

        for i in range(2, numRows + 1):
            temp = [1]
            for j in range(len(result[-1]) -1):
                temp.append(result[-1][j] + result[-1][j + 1])
            temp.append(1)
            result.append(temp)

        return result[-1]

