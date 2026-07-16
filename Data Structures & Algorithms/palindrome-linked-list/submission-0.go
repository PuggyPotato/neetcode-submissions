/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func isPalindrome(head *ListNode) bool {
	stack := make([]int,0)
	curr := head
	for curr != nil {
		stack = append(stack,curr.Val)
		curr = curr.Next
	}
	curr = head
	count := len(stack) - 1
	for curr != nil {
		if curr.Val != stack[count] {
			return false
		}
		count--
		curr = curr.Next
	}
	return true
}
