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
            return head

        oldToNew = {None:None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToNew[cur] = copy
            cur= cur.next

        #loop through oldToNew to properly assign random and next values
        cur = head

        while cur:
            copy = oldToNew[cur]

            copy.next = oldToNew[cur.next]
            copy.random = oldToNew[cur.random]
            
            cur = cur.next

        return oldToNew[head]