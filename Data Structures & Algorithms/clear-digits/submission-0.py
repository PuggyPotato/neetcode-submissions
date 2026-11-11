class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for val in s:
            if val <= '9' and val >= '0':
                stack.pop()
            else:
                stack.append(val)

        return "".join(stack)