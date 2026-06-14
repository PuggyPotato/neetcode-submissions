func isSubsequence(s string, t string) bool {
    slowPtr := 0
    fastPtr := 0
    fullWord := ""
    for fastPtr < len(t) && slowPtr < len(s){
        if t[fastPtr] == s[slowPtr] {
            fullWord += string(t[fastPtr])
            fastPtr +=1
            slowPtr +=1
        } else{
            fastPtr +=1
        }
    }
    return s == fullWord
}
