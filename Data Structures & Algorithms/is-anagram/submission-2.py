class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana1 = {}
        ana2 = {}
        for char in s:
            ana1[char] = ana1.get(char,0) +1

        for char in t:
            ana2[char] = ana2.get(char,0) +1

        if ana1 == ana2:
            return True
        
        return False
        