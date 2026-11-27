class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        # code here
        total = 0

        for i in range(len(adj)):
            total += len(adj[i])

        return total // 2
