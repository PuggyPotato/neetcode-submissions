class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_substring = -1
        hashmap = {}
        for i,val in enumerate(s):
            if val in hashmap:
                temp = i - hashmap[val]
                if temp > max_substring:
                    max_substring = temp - 1
            else:
                hashmap[val] = i

        return max_substring