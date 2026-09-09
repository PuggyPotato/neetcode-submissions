class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = [0] * 26
        n = len(words)

        for word in words:
            for i in range(len(word)):
                freq[ord(word[i]) - 97] += 1


        for char in freq:
            if char % n != 0:
                return False

        return True