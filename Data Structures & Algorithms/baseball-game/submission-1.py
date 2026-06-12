class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for i,val in enumerate(operations):
            print(stack)
            if val == "+":
                total += int(stack[len(stack)-2]) + int(stack[len(stack)-1])
                stack.append(int(stack[len(stack)-2]) + int(stack[len(stack)-1]))
            elif val == "D":
                total += int(stack[len(stack)-1]) * 2
                stack.append(int(stack[len(stack)-1]) * 2)
            elif val == "C":
                temp = stack.pop()
                total -= int(temp) 
            else:
                stack.append(val)
                total += int(val)
                #print("triggered")
        return total
        