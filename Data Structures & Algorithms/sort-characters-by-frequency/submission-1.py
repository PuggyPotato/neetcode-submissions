class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s).most_common()

        return "".join(char * freq for char, freq in counter)