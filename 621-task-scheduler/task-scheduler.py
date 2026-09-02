class Solution(object):
    def leastInterval(self, tasks, n):
        # Count frequencies of each task
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        # Find the maximum frequency of any task
        max_freq = max(freq)
        
        # Count how many tasks have this maximum frequency
        max_count = 0
        for f in freq:
            if f == max_freq:
                max_count += 1
                
        # Calculate the minimum intervals required by the formula
        intervals = (max_freq - 1) * (n + 1) + max_count
        
        # The answer cannot be less than the total number of tasks
        return max(len(tasks), intervals)
