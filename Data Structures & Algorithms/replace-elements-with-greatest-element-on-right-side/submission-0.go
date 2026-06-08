func replaceElements(arr []int) []int {
	for i:=0; i < len(arr); i++ {

		if i == len(arr) -1 {
			arr[i] = -1
			continue
		}

		maximum := arr[i+1]

		for j:=i+1; j < len(arr); j++ {
			if arr[j] > maximum {
				print(arr[j], maximum,"\n")
				maximum = arr[j]
			}
		}

		arr[i] = maximum
	}
	return arr
}
