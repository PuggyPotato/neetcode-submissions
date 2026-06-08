func twoSum(nums []int, target int) []int {
    notebook := make(map[int]int)

    for i,value := range nums{
        complement := target - value
        if index,ok := notebook[complement]; ok{
            return []int{index,i} 
        }
        notebook[value] = i
    }
    return []int{}
}
