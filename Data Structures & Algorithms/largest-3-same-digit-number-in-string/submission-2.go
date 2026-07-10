
func largestGoodInteger(num string) string {
	ptrFast := 0
	ptrSlow := 0
	answer := ""
	hasValue := false
	for ptrFast < len(num) - 2 {
		if num[ptrFast] == num[ptrFast+1]  && num[ptrFast] == num[ptrFast+2] {
			if !hasValue {
				answer = string(num[ptrFast]) + string(num[ptrFast]) + string(num[ptrFast])
				hasValue = true
			}
			if num[ptrFast] > num[ptrSlow] {
				answer = string(num[ptrFast]) + string(num[ptrFast]) + string(num[ptrFast])
				ptrSlow = ptrFast
			}
		}
		ptrFast++
	}
	return answer
}
