"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store = {}
        curr = head
        while curr:
            store[curr] = Node(curr.val)
            curr = curr.next
        
        copyHead = store.get(head, None)
        curr = head
        while curr:
            copy = store[curr]
            copy.next = store.get(curr.next, None)
            copy.random = store.get(curr.random, None)
            curr = curr.next

        return copyHead