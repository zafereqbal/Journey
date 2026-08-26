class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for i in range(n):
            fast = fast.next

        # Move both until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node
        slow.next = slow.next.next

        return dummy.next