func mergeAlternately(word1 string, word2 string) string {
	word1Ptr :=0
	word2Ptr :=0 
	fullWord := ""
	for word1Ptr < len(word1) || word2Ptr < len(word2) {
		if word1Ptr < len(word1) && word2Ptr < len(word2) {
			fullWord = fullWord + string(word1[word1Ptr]) + string(word2[word2Ptr])
			word1Ptr++
			word2Ptr++
		} else if word1Ptr < len(word1) {
			fullWord = fullWord + string(word1[word1Ptr:])
			break
		} else {
			fullWord = fullWord + string(word2[word2Ptr:])
			break
		}
	}
	return fullWord
}
