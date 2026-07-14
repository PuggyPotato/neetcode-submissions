func numUniqueEmails(emails []string) int {
    seenEmail := make(map[string]struct{})
	count := 0

	for _, email := range emails {
		fullEmail := ""

		for i:=0; i < len(email); i++ {
			if email[i] == '@' {
				fullEmail += email[i:]
				break
			}

			if email[i] == '.' {
				
			} else if email[i] == '+' {
				for email[i+1] != '@' {
					i++
				}
			} else {
				fullEmail += string(email[i])
			}

		}

		if _, ok := seenEmail[fullEmail]; !ok {
			count++
		}

		seenEmail[fullEmail] = struct{}{}
	}
	return count
}