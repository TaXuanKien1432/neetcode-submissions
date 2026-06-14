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
        
        curr = head
        while curr:
            copy = store[curr]
            copy.next = store.get(curr.next)
            copy.random = store.get(curr.random)
            curr = curr.next

        return store.get(head)