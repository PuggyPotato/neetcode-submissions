func removeDuplicates(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    seen := make(map[int]bool)
    
    writeIndex := 0

    for _, val := range nums {
        if !seen[val] {
            seen[val] = true
            nums[writeIndex] = val
            writeIndex++
        }
    }
    return writeIndex
}