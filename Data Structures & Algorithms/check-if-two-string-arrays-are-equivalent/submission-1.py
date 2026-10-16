from itertools import chain, zip_longest
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return all(c1 == c2 for c1, c2 in zip_longest(chain.from_iterable(word1), chain.from_iterable(word2)))
