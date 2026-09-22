class Solution:
    def compress(self, chars: List[str]) -> int:
        ptr = 0

        slow = 0
        count = 0

        for fast in range(len(chars)):

            if fast + 1 == len(chars) or chars[fast] != chars[fast + 1]:
                chars[ptr] = chars[slow]
                ptr += 1

                count = fast - slow + 1
                if count > 1:
                    for val in str(count):
                        chars[ptr] = val
                        ptr += 1

                slow = fast + 1

        return ptr


            