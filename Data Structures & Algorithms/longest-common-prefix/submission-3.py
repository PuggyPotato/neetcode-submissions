class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        wordPtr = 0
        charPtr = 0
        longest = ""
        while wordPtr < len(strs):

            if charPtr >= len(strs[wordPtr]) or charPtr >= len(first_word):
                break

            if strs[wordPtr][charPtr] != first_word[charPtr]:
                break

            else:
                if wordPtr == len(strs) -1:
                    longest += first_word[charPtr]
                    charPtr +=1 
                    wordPtr = 0
                    
            wordPtr +=1
            if wordPtr >= len(strs):
                wordPtr = 0

        return longest