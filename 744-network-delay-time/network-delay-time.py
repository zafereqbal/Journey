import collections
import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # 1. Build the adjacency list graph
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # 2. Initialize the priority queue (min-heap) with (distance, node)
        # We start at node k with a distance/time of 0
        pq = [(0, k)]
        
        # Dictionary to track the shortest time to reach each node
        dist = {}
        
        # 3. Process the graph using Dijkstra's algorithm
        while pq:
            d, node = heapq.heappop(pq)
            
            # If we've already found the shortest path to this node, skip it
            if node in dist:
                continue
            dist[node] = d
            
            # Explore neighbors
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (d + weight, neighbor))
                    
        # 4. Check if all n nodes were reached
        # If yes, the total time is the maximum of all shortest path distances
        return max(dist.values()) if len(dist) == n else -1
