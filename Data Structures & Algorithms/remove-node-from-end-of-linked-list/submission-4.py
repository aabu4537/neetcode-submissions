# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        counter = 0
        while curr:
            curr = curr.next
            counter+=1
        
        actual = counter - n

        i = 0
        curr = head
        prev = None
        while i < actual:
            prev = curr
            curr = curr.next
            i+=1
        
        if not prev:
            return head.next

        prev.next = curr.next
        return head
        
        
        