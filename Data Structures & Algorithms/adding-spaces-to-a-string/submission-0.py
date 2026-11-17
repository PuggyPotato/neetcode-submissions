class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        ptr = 0
        for i, val in enumerate(s):
            if ptr < len(spaces) and i == spaces[ptr]:
                result += " "
                ptr += 1
            result += val

        return result 
