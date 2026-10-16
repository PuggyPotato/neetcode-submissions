class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        ptr = 0
        count = 0
        max_count = 0

        while ptr < len(tokens):
            if power - tokens[ptr] < 0:
                power += tokens[-1]
                tokens.pop(-1)
                if count == 0:
                    return 0
                count -= 1
            else:
                power -= tokens[ptr]
                count += 1
                ptr += 1
                max_count = max(max_count, count)

        return max_count