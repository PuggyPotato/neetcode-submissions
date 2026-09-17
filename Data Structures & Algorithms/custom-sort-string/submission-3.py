class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        result = []

        for val in order:
            if val in counter:
                result.append(val * counter[val])
                del(counter[val])

        for val in counter:
            result.append(val * counter[val])


        return "".join(result)