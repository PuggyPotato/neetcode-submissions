class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = [0] * 26
        n = len(words)

        for word in words:
            for char in word:
                freq[ord(char) - 97] += 1


        for count in freq:
            if count % n != 0:
                return False

        return True