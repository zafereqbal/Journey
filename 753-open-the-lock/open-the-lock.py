from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead_set = set(deadends)
        
        # If the starting point is blocked, we cannot proceed
        if "0000" in dead_set:
            return -1
        if target == "0000":
            return 0
            
        # Queue stores tuples of (current_combination, current_turns)
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        
        while queue:
            current, turns = queue.popleft()
            
            # Check if we reached the target combination
            if current == target:
                return turns
                
            # Generate all 8 possible next combinations
            for i in range(4):
                digit = int(current[i])
                
                # Turn wheel forward (+1) and backward (-1)
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    neighbor = current[:i] + str(new_digit) + current[i+1:]
                    
                    # If the neighbor is valid and not visited, add to queue
                    if neighbor not in dead_set and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, turns + 1))
                        
        return -1
