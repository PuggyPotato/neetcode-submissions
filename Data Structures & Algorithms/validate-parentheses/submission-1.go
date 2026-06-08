func isValid(s string) bool {
    var stack []rune
	for _, val := range s {
		if len(stack) > 0 {
			topElement := stack[len(stack) -1]
			if val == ')' && topElement == '(' {
				stack = stack[:len(stack) -1]
				continue
			}
			if val == ']' && topElement == '[' {
				stack = stack[:len(stack) -1]
				continue
			}
			if val == '}' && topElement == '{' {
				stack = stack[:len(stack) -1]
				continue
			}
			stack = append(stack,val)
		} else {
			stack = append(stack, val)
		}
	}

	if len(stack) > 0 {
		return false
	}

	return true
}
