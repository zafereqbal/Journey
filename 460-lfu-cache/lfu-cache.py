from collections import defaultdict, OrderedDict

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.min_freq = 0
        # Maps key -> [value, frequency]
        self.key_to_val_freq = {}
        # Maps frequency -> OrderedDict of keys (maintains LRU order)
        self.freq_to_keys = defaultdict(OrderedDict)

    def _update_freq(self, key):
        val, freq = self.key_to_val_freq[key]
        
        # Remove key from current frequency bucket
        del self.freq_to_keys[freq][key]
        
        # If this bucket is now empty and was the minimum frequency, increment min_freq
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
                
        # Add key to the next frequency bucket
        new_freq = freq + 1
        self.key_to_val_freq[key][1] = new_freq
        self.freq_to_keys[new_freq][key] = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_val_freq:
            return -1
        
        self._update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Edge case: capacity is 0
        if self.capacity <= 0:
            return

        # Case 1: Key already exists -> update value and frequency
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key][0] = value
            self._update_freq(key)
            return

        # Case 2: Cache is full -> evict the least frequently & least recently used key
        if len(self.key_to_val_freq) >= self.capacity:
            # popitem(last=False) removes the oldest (LRU) key in the min_freq bucket
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

        # Insert new key with frequency 1
        self.key_to_val_freq[key] = [value, 1]
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
