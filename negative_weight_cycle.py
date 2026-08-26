class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        # code here
        # Start all distances at 0 so that we can detect
        # negative cycles in any component of the graph.
        dist = [0] * V
        # Relax all edges V-1 times
        for _ in range(V - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break
        # If we can still relax an edge after V-1 iterations,
        # a negative weight cycle exists.
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                return True
        return False
