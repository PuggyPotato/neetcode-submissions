func appendCharacters(s string, t string) int {
    first := 0
	second := 0
	
	for first < len(s) && second < len(t) {
		if s[first] == t[second] {
			first++
			second++
		} else {
			first++
		}
	}
	return len(t) - second
}