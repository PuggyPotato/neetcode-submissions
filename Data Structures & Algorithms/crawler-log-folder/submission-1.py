class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for val in logs:
            if stack and val == "../":
                stack.pop()
            elif val == "../":
                pass
            elif val == "./":
                pass
            else:
                stack.append(1)

        return len(stack)