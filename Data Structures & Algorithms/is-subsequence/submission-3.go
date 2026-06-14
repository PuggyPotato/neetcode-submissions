func isSubsequence(s string, t string) bool {
    slowPtr := 0
    fastPtr := 0
    for fastPtr < len(t) && slowPtr < len(s){
        if t[fastPtr] == s[slowPtr] {
            slowPtr +=1
        } 
        fastPtr +=1
    }
    return slowPtr == len(s)
}
