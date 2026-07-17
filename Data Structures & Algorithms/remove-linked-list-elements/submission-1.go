/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func removeElements(head *ListNode, val int) *ListNode {
	dummy := &ListNode{}
	currHead := head
	currDummy := dummy

	for currHead != nil {

		if currHead.Val != val {
			currDummy.Next = &ListNode{Val:currHead.Val}
			currDummy = currDummy.Next
		}
		currHead = currHead.Next
	}
	return dummy.Next

}
