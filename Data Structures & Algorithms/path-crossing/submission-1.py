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

            seenTup = (x,y)
            if seen.get(seenTup):
                return True

            seen[seenTup] = True

        return False