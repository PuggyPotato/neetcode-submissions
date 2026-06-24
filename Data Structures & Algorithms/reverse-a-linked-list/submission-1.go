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
        tempNext := curr.Next
        curr.Next = prev
        prev = curr
        curr = tempNext
    }
    return prev
}
