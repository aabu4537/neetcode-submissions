# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Split the list into two halves using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # second starts right after the middle node
        second = slow.next
        # Sever the connection to break them into two separate lists
        slow.next = None

        # Step 2: Reverse the second half of the list
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 'prev' is now the head of the reversed second half
        # 'head' is the head of the first half

        # Step 3: Merge (interleave) the two halves together
        first_half = head
        second_half = prev  # This was 'prev' after the reversal loop finished

        while second_half:
            # Temporarily store the next nodes to avoid losing them
            temp1 = first_half.next
            temp2 = second_half.next

            # Connect first half node to second half node
            first_half.next = second_half
            # Connect second half node to the next first half node
            second_half.next = temp1

            # Advance the pointers for the next iteration
            first_half = temp1
            second_half = temp2
