func canConstruct(ransomNote string, magazine string) bool {
	seen := make([]int,26)
	for _,val := range magazine {
		seen[val - 'a']++
	}

	for _, val := range ransomNote {
		seen[val - 'a']--
		if seen[val - 'a'] < 0 {
			return false
		}
	}	
	return true
}
