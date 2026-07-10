
func largestGoodInteger(num string) string {
	ptrFast := 0
	var maxChar byte
	answer := ""
	hasValue := false
	for ptrFast < len(num) - 2 {
		if num[ptrFast] == num[ptrFast+1]  && num[ptrFast] == num[ptrFast+2] {
			if !hasValue {
				answer = string(num[ptrFast]) + string(num[ptrFast]) + string(num[ptrFast])
				hasValue = true
			}
			if num[ptrFast] > maxChar {
				answer = string(num[ptrFast]) + string(num[ptrFast]) + string(num[ptrFast])
				maxChar = num[ptrFast]
			}
		}
		ptrFast++
	}
	return answer
}
