# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use fast and slow pointer to find midpoint
        # when fast pointer.next is null or is on a null node

        # slow pointer is at the midpoint

        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next
        
        # now found the mid point

        # reverse

        curr = slow.next
        slow.next = None
        prev = None

        while curr:

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head1 = head
        head2 = prev

        while head2:

            swap1 = head1.next
            swap2 = head2.next

            head1.next = head2
            head2.next = swap1

            head1 = swap1
            head2 = swap2

            

        

        
