class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for val in s:
            if val == "(":
                stack.append(val)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(val)

        return len(stack)
