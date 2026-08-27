class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge the two halves
        first = head
        second = prev

        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2