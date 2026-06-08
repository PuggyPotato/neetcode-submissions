func isAnagram(s string, t string) bool {
    notebook := make(map[rune]int)
    if len(s) != len(t){
        return false
    }
    for _,value := range s{
        notebook[value]++
    }
    for _,value := range t{
        notebook[value]--
    }
    for _,value := range notebook{
        if value !=0{
            return false
        }
    }
    return true
}
