func kthDistinct(arr []string, k int) string {
	
	seen := make(map[string]int)

	for _, val := range arr {
		seen[val]++
	}

	for _,value := range arr {
		if seen[value] == 1 {
			k--
		}
		if k == 0 {
			return value
		}
	}


	return ""
}