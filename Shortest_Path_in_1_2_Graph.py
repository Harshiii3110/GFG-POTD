import heapq
class Solution:
    def shortestPath(self, V: int, src: int, dest: int, edges: list[list[int]]) -> int:
        # code here
        graph = [[] for _ in range(V)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        dist = [float('inf')] * V
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            if node == dest:
                return d
            for nei, wt in graph[node]:
                if d + wt < dist[nei]:
                    dist[nei] = d + wt
                    heapq.heappush(pq, (dist[nei], nei))
        return -1 if dist[dest] == float('inf') else dist[dest]        
