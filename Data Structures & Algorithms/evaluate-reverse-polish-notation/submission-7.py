class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            count = 0
            if val != "+" and val != "-" and val != "*" and val != "/":
                stack.append(val)
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if val == "+":
                    count += int(val1) + int(val2)
                elif val == "-":
                    count += int(val2) - int(val1)
                elif val == "*":
                    count += int(val1) * int(val2)
                elif val == "/":
                    count += int(val2) / int(val1)
                    
                stack.append(count)

        return int(stack[0])