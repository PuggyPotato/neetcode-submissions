/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    var prev *ListNode = nil
    curr := head
    
    for curr != nil {
        nextNode := curr.Next 
        curr.Next = prev      
        prev = curr          
        curr = nextNode       
    }
    
    return prev
}
