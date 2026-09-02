class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for value in asteroids:
            if stack and value < 0:
                if stack[-1] < 0:
                    stack.append(value)
                    continue

                while stack and stack[-1] > 0 and abs(value) > stack[-1]:
                    stack.pop()


                if stack and stack[-1] > 0 and abs(value) == stack[-1]:
                    stack.pop()
                    continue
                elif stack and stack[-1] < 0:
                    stack.append(value)
                    
                if not stack:
                    stack.append(value)
                
            else:
                stack.append(value)

        return stack