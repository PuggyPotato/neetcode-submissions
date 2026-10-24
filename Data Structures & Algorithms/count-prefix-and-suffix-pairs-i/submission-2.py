class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                w = words[i]
                if words[j].startswith(w) and words[j].endswith(w):
                    count += 1

        return count