func validPalindrome(s string) bool {
	left := 0
	right := len(s) - 1
	for left < right {
		if s[left] != s[right] {
			break
		}
		left++
		right--
	}
	return isPalindrome(s,left+1,right) || isPalindrome(s,left,right-1)
}

func isPalindrome(s string,left int,right int) bool {
	for left < right {
		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}
	return true
}
