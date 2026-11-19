class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # Step 1: Map each character to its last index in the string
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        partitions = []
        start = 0
        end = 0
        
        # Step 2: Greedily expand the current partition boundary
        for idx, char in enumerate(s):
            end = max(end, last_occurrence[char])
            
            # Step 3: If current index reaches the boundary, finalize the partition
            if idx == end:
                partitions.append(end - start + 1)
                start = idx + 1
                
        return partitions
