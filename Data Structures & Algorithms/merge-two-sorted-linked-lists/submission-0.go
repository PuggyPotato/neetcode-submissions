/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    dummy := &ListNode{}
    head1 := list1
    head2 := list2
    tail := dummy
    for head1 != nil || head2 != nil {
        if head1 != nil && head2 != nil{
            if head1.Val < head2.Val {
                nextNode := &ListNode{Val:head1.Val}
                tail.Next = nextNode
                tail = tail.Next
                head1 = head1.Next
            } else {
                nextNode := &ListNode{Val:head2.Val}
                tail.Next = nextNode
                tail = tail.Next
                head2 = head2.Next
            }
        } else if head1 != nil {
            nextNode := &ListNode{Val:head1.Val}
            tail.Next = nextNode
            tail = tail.Next
            head1 = head1.Next
        } else {
            nextNode := &ListNode{Val:head2.Val}
            tail.Next = nextNode
            tail = tail.Next
            head2 = head2.Next
        }
    }
    return dummy.Next
}
