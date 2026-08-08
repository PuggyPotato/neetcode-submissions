class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()

        if len(pattern) != len(word):
            return False
        
        pattern_to_s = {}
        word_to_pattern = {}
        for i in range(len(word)):
            if pattern[i] in pattern_to_s and pattern_to_s[pattern[i]] != word[i]:
                return False
            
            if word[i] in word_to_pattern and word_to_pattern[word[i]] != pattern[i]:
                return False

            pattern_to_s[pattern[i]] = word[i]
            word_to_pattern[word[i]] = pattern[i]

        return True
            