# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base case: if the list is empty or has only one element, it is already sorted
        if not head or not head.next:
            return head
        
        # Step 1: Split the linked list into two halves using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None  # Cut the list into two distinct halves
        
        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Step 3: Merge the two sorted halves
        return self.merge(left, right)
        
    def merge(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Append the remaining nodes of whichever list is left over
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        return dummy.next
