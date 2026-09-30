# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        first = head

        prev = None
        cur = second
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        second = prev

        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        


