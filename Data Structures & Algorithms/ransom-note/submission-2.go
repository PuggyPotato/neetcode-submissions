func canConstruct(ransomNote string, magazine string) bool {
	count := make([]int,26)
	for _,val := range magazine {
		count[val - 'a']++
	}

	for _, val := range ransomNote {
		count[val - 'a']--
		if count[val - 'a'] < 0 {
			return false
		}
	}	
	return true
}
