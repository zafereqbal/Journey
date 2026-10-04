class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = [i for i in range(n + 1)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return [a, b]

            parent[rootA] = rootB