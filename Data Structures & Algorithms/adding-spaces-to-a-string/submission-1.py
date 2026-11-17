class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = list()
        ptr = 0
        for i, val in enumerate(s):
            if ptr < len(spaces) and i == spaces[ptr]:
                result.append(" ")
                ptr += 1
            result.append(val)

        return "".join(result)
