class Solution:
    def getRow(self, numRows: int) -> List[List[int]]:
        result = []

        if numRows == 0:
            return [1]
        elif numRows == 1:
            return [1,1]

        for i in range(1, numRows + 1):
            temp = [1]
            for j in range(len(result) -1):
                temp.append(result[j] + result[j + 1])
            temp.append(1)
            result = temp

        return result

