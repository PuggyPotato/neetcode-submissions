func lengthOfLongestSubstring(s string) int {
	charIndex := make(map[byte]int)
	maxLength := 0
	left := 0	
	for right := 0; right < len(s); right++ {
		char := s[right]
		if index, ok := charIndex[char]; ok && index >= left {
			left = index + 1
		}
		if right - left + 1 > maxLength {
			maxLength = right - left + 1
		}
		charIndex[s[right]] = right
	}
	return maxLength
}
