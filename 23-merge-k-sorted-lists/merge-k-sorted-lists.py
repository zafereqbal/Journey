import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Custom comparison wrapper for ListNode to avoid comparison errors in Python 3
        # when two nodes have the exact same value.
        class HeapNode:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        min_heap = []
        
        # Push the head of each non-empty linked list into the heap
        for l in lists:
            if l:
                heapq.heappush(min_heap, HeapNode(l))
                
        # Create a dummy head to easily build the merged list
        dummy = ListNode(0)
        curr = dummy
        
        # Process the heap until it is empty
        while min_heap:
            # Get the smallest node currently available
            heap_node = heapq.heappop(min_heap)
            smallest_node = heap_node.node
            
            # Append it to our merged list
            curr.next = smallest_node
            curr = curr.next
            
            # If the extracted node has a next node, push it into the heap
            if smallest_node.next:
                heapq.heappush(min_heap, HeapNode(smallest_node.next))
                
        return dummy.next
