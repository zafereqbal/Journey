class TimeMap(object):

    def __init__(self):
        # Initialize a dictionary to map each key to a list of (timestamp, value) pairs
        self.store = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        # Since timestamps are strictly increasing, the list remains sorted
        self.store[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:
            return ""
        
        pairs = self.store[key]
        left, right = 0, len(pairs) - 1
        res = ""
        
        # Binary search to find the largest timestamp <= the given timestamp
        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]  # Candidate answer found, try to look for a closer one
                left = mid + 1
            else:
                right = mid - 1
                
        return res
