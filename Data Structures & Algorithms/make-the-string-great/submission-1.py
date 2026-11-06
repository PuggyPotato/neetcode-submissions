class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for val in s:
            if stack and stack[-1] != val and val.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(val)

        return "".join(stack)