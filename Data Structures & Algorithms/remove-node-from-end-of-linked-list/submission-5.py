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
        dummy = ListNode(0, head)
        curr = head
        prev = dummy
        for i in range(actual):
            curr = curr.next
            prev = prev.next
        
        prev.next = curr.next
        return dummy.next
            
        
        
        