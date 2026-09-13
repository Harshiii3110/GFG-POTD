from collections import deque
class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        # code here
        n = len(adj)
        def bfs(start):
            dist = [-1] * n
            dist[start] = 0
            q = deque([start])
            farthest = start
            while q:
                u = q.popleft()
                for v in adj[u]:
                    v -= 1  # Convert 1-based house number to 0-based index
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
                        if dist[v] > dist[farthest]:
                            farthest = v
            return farthest, dist[farthest]
        # Find one endpoint of the tree diameter
        a, _ = bfs(0)
        # Find the diameter length
        _, diameter = bfs(a)
        # Minimum maximum distance from the center
        return (diameter + 1) // 2
