class Solution:
    
    def validPalindrome(self, s: str) -> bool:

        def tryDelete(left_ptr,right_ptr) -> bool:
            while left_ptr < right_ptr:
                if s[left_ptr] != s[right_ptr]:
                    return False

                left_ptr += 1
                right_ptr -= 1
            return True


        left_ptr = 0
        right_ptr = len(s) - 1
        while left_ptr < right_ptr:
            if s[left_ptr] != s[right_ptr]:
                return tryDelete(left_ptr + 1, right_ptr) or tryDelete(left_ptr, right_ptr - 1)

            left_ptr += 1
            right_ptr -= 1

        return True

