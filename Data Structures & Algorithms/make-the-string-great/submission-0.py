class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for val in s:
            if stack:
                if val.upper() == val and stack[-1] == val.lower():
                    stack.pop()
                elif val.lower() == val and stack[-1] == val.upper():
                    stack.pop()
                else:
                    stack.append(val)
            else:
                stack.append(val)

        return "".join(stack)
