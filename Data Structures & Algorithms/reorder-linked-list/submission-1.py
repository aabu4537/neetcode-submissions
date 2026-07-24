# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        prev = None
        curr = second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first = head
        second = prev
        dummy = ListNode(0)
        curr = dummy

        while first and second:
            curr.next = first
            first = first.next
            curr = curr.next

            curr.next = second
            second = second.next
            curr = curr.next
            print(curr.val)

        if first:
            curr.next = first
            
        head = dummy.next
        
        