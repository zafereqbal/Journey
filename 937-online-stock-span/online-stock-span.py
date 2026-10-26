class StockSpanner(object):

    def __init__(self):
        # The stack will store tuples of (price, span)
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        # Every day has at least a span of 1 (itself)
        span = 1
        
        # Pop elements from stack while the top price is <= current price
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
            
        # Push the current price and its accumulated span onto the stack
        self.stack.append((price, span))
        
        return span
