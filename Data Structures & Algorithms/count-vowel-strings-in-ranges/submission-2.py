class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = {"a", "e", "i", "o", "u"}

        prefix = [0] * (len(words) + 1)

        count = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            prefix[i + 1] = count

        result = [0] * len(queries)
        for i, (left, right) in enumerate(queries):
            result[i] = prefix[right + 1] - prefix[left]

        return result