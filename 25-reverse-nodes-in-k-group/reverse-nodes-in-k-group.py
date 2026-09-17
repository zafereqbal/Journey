# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Count the total length of the linked list
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        # Dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        
        # Pointers to track the boundaries of groups
        group_prev = dummy
        curr = head
        
        # Loop through the list while there are at least k nodes remaining
        while count >= k:
            prev = None
            group_tail = curr  # The current node will become the tail of this reversed group
            
            # Reverse k nodes
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # Connect the previous group's tail to the new head of this reversed group
            group_prev.next = prev
            
            # Connect the tail of this reversed group to the next remaining part of the list
            group_tail.next = curr
            
            # Move group_prev forward to prepare for the next iteration
            group_prev = group_tail
            
            # Decrease the remaining count by k
            count -= k
            
        return dummy.next
