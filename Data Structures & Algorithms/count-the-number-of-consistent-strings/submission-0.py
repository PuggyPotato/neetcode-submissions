class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        seen = {}
        count = len(words)
        for char in allowed:
            seen[char] = True

        for word in words:
            for i in range(len(word)):
                if word[i] not in seen:
                    count -= 1
                    break

        return count