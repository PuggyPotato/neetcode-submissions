class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        arr = [0] * 26
        count = len(words)
        for char in allowed:
            arr[ord(char) - ord('a')] = True


        for word in words:
            for i in range(len(word)):
                if arr[ord(word[i]) - ord('a')] == False:
                    count -= 1
                    break
                    
        return count