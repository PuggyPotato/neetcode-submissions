class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            count = 0
            if val == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                count += int(val1) + int(val2)
                stack.append(count)
            elif val == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                count += int(val2) - int(val1)
                stack.append(count)
            elif val == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                count += int(val1) * int(val2)
                stack.append(count)
            elif val == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                count += int(val2) / int(val1)
                stack.append(count)
            else:
                stack.append(int(val))

        return int(stack[0])