# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        cur = head 

        while cur:
            cur = cur.next
            count +=1
        
        count = count - n+1
        dummy = ListNode(-1, head)
        prev = cur = dummy
        
        for i in range(count):
            prev = cur
            cur = cur.next
        
        prev.next = cur.next 
        
        return dummy.next
