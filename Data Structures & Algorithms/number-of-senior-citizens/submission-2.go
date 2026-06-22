func countSeniors(details []string) int {
	count := 0
    for _, word := range details {
		age := (int(word[11])- '0') * 10 + (int(word[12]) -'0')
		if age > 60 {
			count++
		}
	}
	return count
}