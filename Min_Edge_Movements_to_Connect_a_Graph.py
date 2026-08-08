class Solution:
    def minEdgesReq(self, n, edges):
        # code here
        parent = list(range(n))
        size = [1] * n
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
            return True
        components = n
        extra = 0
        for u, v in edges:
            if union(u, v):
                components -= 1
            else:
                extra += 1
        if extra < components - 1:
            return -1
        return components - 1
