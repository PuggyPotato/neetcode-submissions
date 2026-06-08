func isPalindrome(s string) bool {
	leftPtr := 0
	rightPtr := len(s) -1

	for leftPtr < rightPtr {
		for !isAlphaNum(rune(s[leftPtr])) && (leftPtr < rightPtr) {
			leftPtr+=1
		}
		for !isAlphaNum(rune(s[rightPtr])) && (leftPtr < rightPtr) {
			rightPtr-=1
		}
		if unicode.ToLower(rune(s[leftPtr])) != unicode.ToLower(rune(s[rightPtr])) {
			return false
		}
		rightPtr -=1
		leftPtr +=1
	}
	return true
}

func isAlphaNum(input rune) bool{
	return unicode.IsDigit(input) || unicode.IsLetter(input)
}

