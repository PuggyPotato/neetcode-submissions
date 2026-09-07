class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0

        seen = {(x, y): True}

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

            seen[(x,y)] = True

        return False