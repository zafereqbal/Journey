# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head2: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        pA = headA
        pB = headB
        
        # Loop continues until both pointers meet (either at the node or at None)
        while pA != pB:
            # Switch to the other list's head when reaching the end
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
            
        return pA
