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
        CopyNode = {None: None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            CopyNode[curr] = copy
            curr = curr.next
            
        curr = head
        while curr:
            copy = CopyNode[curr]
            copy.next = CopyNode[curr.next]
            copy.random = CopyNode[curr.random]
            curr = curr.next
        
        return CopyNode[head]