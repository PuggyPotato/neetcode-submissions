class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for val in s:
            if val == "B" and stack and stack[-1] == "A":
                stack.pop()
            elif val == "D" and stack and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(val)

        return len(stack)