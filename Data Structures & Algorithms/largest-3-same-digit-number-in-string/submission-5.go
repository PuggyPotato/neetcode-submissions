
func largestGoodInteger(num string) string {
	var maxChar byte = 0
	for i := 0; i < len(num) - 2; i++ {
		if num[i] == num[i+1] && num[i] == num[i+2] {
			if num[i] > maxChar {
				maxChar = num[i]
			}
		}
	}
	if maxChar == 0 {
		return ""
	}
	return string([]byte{maxChar,maxChar,maxChar})
}
