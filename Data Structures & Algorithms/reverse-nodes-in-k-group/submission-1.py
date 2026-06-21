# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        prevTail = dummy
        h = 0
        curr = head
        while curr:
            h += 1
            if h == k:
                h = 0
                newHead = curr.next
                curr.next = None
                currHead, currTail = self.reverse(head)
                prevTail.next = currHead
                prevTail = currTail
                head = newHead
                curr = head
                continue
            curr = curr.next
        prevTail.next = head
        return dummy.next

    def reverse(self, head):
        prev, curr = ListNode(), head
        currTail = curr
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return (prev, currTail)
