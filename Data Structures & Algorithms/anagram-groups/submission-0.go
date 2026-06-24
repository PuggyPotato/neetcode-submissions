func groupAnagrams(strs []string) [][]string {
	hashMap := make(map[[26]int][]string)
	for _, word := range strs {
		var char [26]int
		for _,val := range word {
			char[val - 'a']++
		}
		hashMap[char] = append(hashMap[char], word)
	}
	result := [][]string{}

	for _, value := range hashMap {
		result = append(result, value)
	}

	return result
}
