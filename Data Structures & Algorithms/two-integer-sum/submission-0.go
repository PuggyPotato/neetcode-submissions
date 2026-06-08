func twoSum(nums []int, target int) []int {
    notebook := make(map[int]int)
    for i:=0;i<len(nums);i++{
        complement := target - nums[i]
        if index,exist := notebook[complement]; exist{
            return []int{index,i}
        }
        notebook[nums[i]] = i
    }
    return []int{}
}
