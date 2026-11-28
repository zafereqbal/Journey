class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        max_factor = max(f for f, _ in items)
        min_price = min(p for _, p in items)
        
        # Count frequency of each factor
        freq = [0] * (max_factor + 1)
        for f, _ in items:
            freq[f] += 1
            
        # Calculate how many items have a factor divisible by i (sieve approach)
        divisible_count = [0] * (max_factor + 1)
        for i in range(1, max_factor + 1):
            if freq[i] > 0:
                for multiple in range(i, max_factor + 1, i):
                    divisible_count[i] += freq[multiple]
                    
        # Group available "buy 1, get 1 free" opportunities by item price
        # Only worthwhile if the item costs less than 2 * min_price
        bundles_by_price = {}
        for f, p in items:
            if p < 2 * min_price:
                free_gain = divisible_count[f] - 1
                if free_gain > 0:
                    bundles_by_price[p] = bundles_by_price.get(p, 0) + free_gain
                    
        total_items = 0
        
        # Greedily buy the cheapest 2-for-1 bundles first
        for p in sorted(bundles_by_price):
            available = bundles_by_price[p]
            can_buy = min(available, budget // p)
            total_items += 2 * can_buy
            budget -= can_buy * p
            if budget < p:
                break
                
        # Spend any remaining budget on the single cheapest item
        total_items += budget // min_price
        
        return total_items
