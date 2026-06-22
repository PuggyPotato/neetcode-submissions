func countSeniors(details []string) int {
	count := 0
    for _, word := range details {
		age , _ := strconv.Atoi(word[11:13])
		if age > 60 {
			count++
		}
	}
	return count
}