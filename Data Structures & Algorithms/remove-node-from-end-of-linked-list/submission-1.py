# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse the list
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        newHead = prev

        # remove nth node while reversing the list again
        prev, curr = None, newHead
        i = 0
        while curr:
            i += 1
            if i == n:
                if curr.next:
                    nxt = curr.next
                    curr.next = None
                    nxtnxt = nxt.next
                    nxt.next = prev
                    if not nxtnxt:
                        return nxt
                    else:
                        prev = nxt
                        curr = nxtnxt
                else:
                    return prev
            else:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
        
        return prev