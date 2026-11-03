import collections
import heapq

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1. Count the frequency of each character
        counts = collections.Counter(s)
        
        # 2. Build a Max-Heap using negative counts (since Python has a Min-Heap by default)
        max_heap = [[-cnt, char] for char, cnt in counts.items()]
        heapq.heapify(max_heap)
        
        prev_cnt, prev_char = 0, ''
        res = []
        
        # 3. Process characters from the heap
        while max_heap:
            cnt, char = heapq.heappop(max_heap)
            res.append(char)
            
            # If the previously used character still has a remaining count, put it back in the heap
            if prev_cnt < 0:
                heapq.heappush(max_heap, [prev_cnt, prev_char])
            
            # Decrease the current count (adding 1 since counts are negative)
            cnt += 1
            # Save the current character to be pushed back in the next iteration
            prev_cnt, prev_char = cnt, char
            
        res_str = "".join(res)
        
        # If the result string is not the same length as the original, it means a valid rearrangement is impossible
        if len(res_str) != len(s):
            return ""
            
        return res_str
