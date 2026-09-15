class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        arr = [0] * len(words)

        for i, word in enumerate(words):
            if word[0] in "aeiou" and word[-1] in "aeiou":
                arr[i] = 1

        result = [0] * len(queries)

        for i, query in enumerate(queries):
            result[i] = sum(arr[query[0]: query[1] + 1])

        return result