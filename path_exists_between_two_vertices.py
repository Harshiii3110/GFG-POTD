
class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
        visited = [False] * len(adj)

        def dfs(node):
            visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        dfs(u)

        return visited[v]
