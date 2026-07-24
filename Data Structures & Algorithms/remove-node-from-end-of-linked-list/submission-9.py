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
            count+=1
            cur = cur.next

        count = count - n
        c= 0
        prev = None
        cur = head
        while c < count:
            prev = cur
            cur=cur.next
            c+=1
        if prev:
            prev.next = cur.next
        else:
            head = head.next

        return head
        
        