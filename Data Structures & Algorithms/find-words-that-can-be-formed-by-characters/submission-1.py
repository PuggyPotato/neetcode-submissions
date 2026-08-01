class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        counter = Counter(chars)

        for word in words:
            counterDuplicate = counter.copy()
            for char in word:
                if counterDuplicate[char] > 0:
                    counterDuplicate[char] -= 1
                else:
                    break
            else:
                count += len(word)


        return count