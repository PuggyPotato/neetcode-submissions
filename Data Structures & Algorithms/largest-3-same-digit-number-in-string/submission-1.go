
func largestGoodInteger(num string) string {

	ptr1 := 0
	possible := ""
	hasValue := false
	for ptr1 < len(num) - 2 {
		if num[ptr1] == num[ptr1+1] && num[ptr1] == num[ptr1 + 2] {
			possibleInNum,_ := strconv.Atoi(possible)
			if !hasValue {
				possible = string(num[ptr1]) + string(num[ptr1]) + string(num[ptr1])
				hasValue = true
			}
			if possibleInNum < (int(num[ptr1] - '0') * 100 + int(num[ptr1] - '0') * 10 + int(num[ptr1]) - '0') {
				possible = string(num[ptr1]) + string(num[ptr1]) + string(num[ptr1])
			}
		}
		ptr1++
	}
	return possible

}
