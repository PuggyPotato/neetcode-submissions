class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y = 0, 0

        seen = {(0, 0)}

        for val in path:
            if val == "N":
                y += 1
            elif val == "S":
                y -= 1
            elif val == "W":
                x -= 1
            elif val == "E":
                x += 1

            if (x, y) in seen:
                return True

            seen.add((x,y))

        return False