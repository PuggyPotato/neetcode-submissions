func numUniqueEmails(emails []string) int {
    seenEmail := make(map[string]struct{},len(emails))

	for _, email := range emails {
		cleaned := make([]byte, 0 , len(email))

		for i:=0 ; i<len(email); i++ {
			if email[i] == '.' {
				continue
			}

			if email[i] == '@' {
				cleaned = append(cleaned, email[i:]...)
				break
			}

			if email[i] == '+' {
				for i < len(email) && email[i] != '@' {
					i++
				}
				cleaned = append(cleaned,email[i:]...)
				break
			}
			cleaned = append(cleaned,email[i])
		}
		seenEmail[string(cleaned)] = struct{}{}

	}
	return len(seenEmail)
}