class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for val in asteroids:
            while stack and val < 0 and stack[-1] > 0:
                result = stack[-1] + val

                if result > 0:
                    break
                elif result < 0:
                    stack.pop()
                else:
                    stack.pop()
                    break

            else:
                stack.append(val)

        return stack