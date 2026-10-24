class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                #print("X", words[j][:len(words[i])], words[j][-len(words[i]):])
                if words[i] == words[j][:len(words[i])] and words[i] == words[j][-len(words[i]):]:
                    count += 1
                    #print(words[j][:len(words[i])], words[j][-len(words[i]):])

        return count