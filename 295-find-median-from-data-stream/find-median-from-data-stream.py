class MedianFinder(object):

    def __init__(self):
        self.small = []   # max heap
        self.large = []   # min heap

    def addNum(self, num):
        # Add to max heap
        self.small.append(num)
        i = len(self.small) - 1

        while i > 0:
            p = (i - 1) // 2
            if self.small[p] >= self.small[i]:
                break
            self.small[p], self.small[i] = self.small[i], self.small[p]
            i = p

        # Move largest of small to large
        if self.small and self.large and self.small[0] > self.large[0]:
            x = self.small[0]
            self.small[0] = self.small[-1]
            self.small.pop()

            i = 0
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i

                if left < len(self.small) and self.small[left] > self.small[largest]:
                    largest = left
                if right < len(self.small) and self.small[right] > self.small[largest]:
                    largest = right

                if largest == i:
                    break

                self.small[i], self.small[largest] = self.small[largest], self.small[i]
                i = largest

            self._push_min(x)

        # Balance heaps
        if len(self.small) > len(self.large) + 1:
            x = self.small[0]
            self.small[0] = self.small[-1]
            self.small.pop()

            i = 0
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i

                if left < len(self.small) and self.small[left] > self.small[largest]:
                    largest = left
                if right < len(self.small) and self.small[right] > self.small[largest]:
                    largest = right

                if largest == i:
                    break

                self.small[i], self.small[largest] = self.small[largest], self.small[i]
                i = largest

            self._push_min(x)

        elif len(self.large) > len(self.small):
            x = self.large[0]
            self.large[0] = self.large[-1]
            self.large.pop()

            if self.large:
                i = 0
                while True:
                    left = 2 * i + 1
                    right = 2 * i + 2
                    smallest = i

                    if left < len(self.large) and self.large[left] < self.large[smallest]:
                        smallest = left
                    if right < len(self.large) and self.large[right] < self.large[smallest]:
                        smallest = right

                    if smallest == i:
                        break

                    self.large[i], self.large[smallest] = self.large[smallest], self.large[i]
                    i = smallest

            self._push_max(x)

    def _push_min(self, x):
        self.large.append(x)
        i = len(self.large) - 1

        while i > 0:
            p = (i - 1) // 2
            if self.large[p] <= self.large[i]:
                break
            self.large[p], self.large[i] = self.large[i], self.large[p]
            i = p

    def _push_max(self, x):
        self.small.append(x)
        i = len(self.small) - 1

        while i > 0:
            p = (i - 1) // 2
            if self.small[p] >= self.small[i]:
                break
            self.small[p], self.small[i] = self.small[i], self.small[p]
            i = p

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(self.small[0])

        return (self.small[0] + self.large[0]) / 2.0