class Solution:
    def compress(self, chars: List[str]) -> int:
        ptrChars = 0

        slow = 0
        fast = 0
        count = 0

        while fast < len(chars):

            if fast == slow:
                chars[ptrChars] = chars[fast]
                count += 1
                ptrChars += 1
                fast += 1

            elif chars[fast] == chars[slow]:
                count += 1
                fast += 1
            
            else:
                slow = fast
                if count > 1:
                    for val in str(count):
                        chars[ptrChars] = val
                        ptrChars += 1
                count = 0

        if count > 1:
           for val in str(count):
                chars[ptrChars] = val
                ptrChars += 1

        return ptrChars

            