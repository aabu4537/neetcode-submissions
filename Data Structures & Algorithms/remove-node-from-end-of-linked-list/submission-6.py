# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        counter = 0
        curr = head
        while curr:
            curr = curr.next
            counter+=1
        
        actual = counter - n

        dummy = ListNode(None, head)
        d = dummy
        counter = 0
        while counter < actual:
            d = d.next
            counter+=1
        
        d.next = d.next.next

        return dummy.next


