class Solution:
    def maxDistance(self, V, src, edges):
        # code here
        adj = [[] for _ in range(V)]
        indegree = [0] * V
        for u, v, w in edges:
            adj[u].append((v, w))
            indegree[v] += 1
        # Topological sort using Kahn's algorithm
        queue = []
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        topo = []
        front = 0
        while front < len(queue):
            u = queue[front]
            front += 1
            topo.append(u)
            for v, w in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        # INT_MIN for unreachable vertices
        INF_NEG = -10**18
        dist = [INF_NEG] * V
        dist[src] = 0
        # Relax edges in topological order
        for u in topo:
            if dist[u] == INF_NEG:
                continue
            for v, w in adj[u]:
                dist[v] = max(dist[v], dist[u] + w)
        # GFG expects INT_MIN for unreachable vertices
        INT_MIN = -2147483648
        for i in range(V):
            if dist[i] == INF_NEG:
                dist[i] = INT_MIN
        return dist

