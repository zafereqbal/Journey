# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Base case: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # 1. Compute the length of the list and locate the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # 2. Handle cases where k is greater than or equal to length
        k = k % length
        if k == 0:
            return head
            
        # 3. Close the list to form a temporary circular loop
        tail.next = head
        
        # 4. Find the new tail node (length - k steps from the head)
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        # 5. Establish the new head and break the circular connection
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
