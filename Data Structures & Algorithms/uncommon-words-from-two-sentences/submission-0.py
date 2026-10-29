class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap = {}
        result = []

        for val in s1.split():
            hashmap[val] = hashmap.get(val, 0) + 1
        
        for val in s2.split():
            hashmap[val] = hashmap.get(val, 0) + 1

        for key, val in hashmap.items():
            if val == 1:
                result.append(key)

        return result
