# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #split list

        slow = head 
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #flip 2nd

        second = slow.next
        slow.next = None

        prev = None
        cur = second
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        second = prev
        first = head

        #merge


        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


            
        