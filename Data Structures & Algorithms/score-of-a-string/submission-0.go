func scoreOfString(s string) int {
    total := 0
    slowPtr := 0
    fastPtr := 1
    for fastPtr < len(s) {
        print(int(s[fastPtr]) - int(s[slowPtr]),"\n")
        if int(s[fastPtr]) - int(s[slowPtr]) >= 0 {
            total += int(s[fastPtr]) - int(s[slowPtr])
        } else {
            total +=  -(int(s[fastPtr]) - int(s[slowPtr]))
        }
        fastPtr +=1
        slowPtr +=1
    }
    return total
}
