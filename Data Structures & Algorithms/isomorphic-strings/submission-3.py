class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(s)):
            if s[i] in hashmap1 and hashmap1[s[i]] != t[i]:
                return False
            elif t[i] in hashmap2 and hashmap2[t[i]] != s[i]:
                return False
            
            hashmap1[s[i]] = t[i]
            hashmap2[t[i]] = s[i]

        return True

