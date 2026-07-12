func isHappy(n int) bool {
    seen := make(map[int]struct{})
	for {
		currentSum := 0

		for n > 0 {
			lastNumber := n % 10
			currentSum += lastNumber * lastNumber
			n /= 10
		}

		if currentSum == 1 {
			break
		}

		if _, ok := seen[currentSum]; ok {
			return false
		}

		seen[currentSum] = struct{}{}

		n = currentSum
	}
	return true
}
