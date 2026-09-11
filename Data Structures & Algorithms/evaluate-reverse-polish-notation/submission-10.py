class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val not in {"+","-","*","/"}:
                stack.append(int(val))
            else:
                right = stack.pop()
                left = stack.pop()
                if val == "+":
                    stack.append(int(left) + int(right))
                elif val == "-":
                    stack.append(int(left) - int(right))
                elif val == "*":
                    stack.append(int(left) * int(right))
                elif val == "/":
                    stack.append(int(left) / int(right))


        return int(stack[0])