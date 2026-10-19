class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for val in s:
            if val == "#" and stack1:
                stack1.pop()
            elif val != "#":
                stack1.append(val)

        for val in t:
            if val == "#" and stack2:
                stack2.pop()
            elif val != "#":
                stack2.append(val)

        return stack1 == stack2