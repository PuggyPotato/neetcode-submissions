class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val != "+" and val != "-" and val != "*" and val != "/":
                stack.append(val)
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if val == "+":
                    stack.append(int(val1) + int(val2))
                elif val == "-":
                    stack.append(int(val2) - int(val1))
                elif val == "*":
                    stack.append(int(val1) * int(val2))
                elif val == "/":
                    stack.append(int(val2) / int(val1))


        return int(stack[0])