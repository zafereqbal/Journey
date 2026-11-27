class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        min_price = min(price for _, price in items)
        
        # dp[c] = max items obtained by buying at most 1 copy of a subset of items with exact cost c
        dp = [0] * (budget + 1)
        
        for i in range(n):
            factor_i, price_i = items[i]
            if price_i > budget:
                continue
                
            # Calculate total items gained from buying the first copy of item i
            # (1 for item i itself + 1 for every other item j whose factor is divisible by factor_i)
            gain = 1
            for j in range(n):
                if i != j and items[j][0] % factor_i == 0:
                    gain += 1
                    
            # Standard 0/1 Knapsack transition (iterate backwards)
            for c in range(budget, price_i - 1, -1):
                if dp[c - price_i] + gain > dp[c]:
                    dp[c] = dp[c - price_i] + gain
                    
        # Spend any remaining budget (budget - c) on the cheapest item
        max_items = 0
        for c in range(budget + 1):
            extra_copies = (budget - c) // min_price
            if dp[c] + extra_copies > max_items:
                max_items = dp[c] + extra_copies
                
        return max_items
