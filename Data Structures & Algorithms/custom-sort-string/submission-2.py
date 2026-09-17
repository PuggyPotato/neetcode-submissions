class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        string = ""

        for val in order:
            if val in counter:
                string += val * counter[val]
                del(counter[val])

        for val in counter:
            string += val * counter[val]


        return string