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
        if not head:
            return None
        cur = head
        oldToNew = {}

        while cur:
            copy = Node(cur.val)
            oldToNew[cur] = copy
            cur= cur.next
        
        cur = head

        while cur:
            copy = oldToNew[cur]
            if cur.next:
                copy.next = oldToNew[cur.next]
            else:
                copy.next = None
            if cur.random:
                copy.random = oldToNew[cur.random]
            else:
                copy.random = None
            cur = cur.next
        
        return oldToNew[head]
            
        