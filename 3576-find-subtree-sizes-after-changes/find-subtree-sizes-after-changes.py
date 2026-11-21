class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = {}
        
        # First DFS: Find the closest ancestor with the same character
        def find_ancestors(u):
            char = s[u]
            prev_ancestor = last_seen.get(char, -1)
            
            if prev_ancestor != -1:
                new_parent[u] = prev_ancestor
                
            last_seen[char] = u
            for v in adj[u]:
                find_ancestors(v)
                
            # Backtrack
            last_seen[char] = prev_ancestor
            
        find_ancestors(0)
        
        # Build the updated tree
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        
        # Second DFS: Compute subtree sizes
        def get_sizes(u):
            for v in new_adj[u]:
                get_sizes(v)
                ans[u] += ans[v]
                
        get_sizes(0)
        return ans
