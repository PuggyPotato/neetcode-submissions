class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for val in s:
            if val == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif val == ')':
                depth -= 1

        return max_depth