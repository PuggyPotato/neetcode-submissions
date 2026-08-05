class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_a = Counter(s)
        count_b = Counter(t)

        unique_letter = count_b - count_a
        string_result = "".join(unique_letter)

        return string_result