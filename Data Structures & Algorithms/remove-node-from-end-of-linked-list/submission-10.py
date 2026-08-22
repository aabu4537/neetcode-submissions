# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        count = 0

        while cur:
            cur = cur.next
            count+=1
        count = count - n
        cur = head
        i = 0
        prev = None
        while i < count:
            prev = cur
            cur = cur.next
            i+=1
        if prev:
            prev.next = cur.next
        else:
            head = head.next

        return head
        
        
