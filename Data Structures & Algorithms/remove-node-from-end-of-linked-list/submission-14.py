# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = i = 0
        cur = head

        while cur:
            cur = cur.next
            count +=1
        
        count = count - n
        dummy = ListNode(-1, head)
        prev = dummy
        cur = head
        while i < count:
            prev = cur
            cur = cur.next
            i+=1
        
        prev.next = cur.next

        return dummy.next
