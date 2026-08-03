class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        max_odd_value = max(v for v in counter.values() if v % 2 != 0)
        min_even_value = min(v for v in counter.values() if v % 2 == 0)

        return max_odd_value - min_even_value