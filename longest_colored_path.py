class Solution:
    def longestPath(self, s, edges):
        # code here
        n = len(s)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1] * n
        order = [0]
        parent[0] = -2
        for u in order:
            for v in graph[u]:
                if parent[v] == -1:
                    parent[v] = u
                    order.append(v)
        down = [1] * n
        for u in reversed(order):
            best = 0
            for v in graph[u]:
                if parent[v] == u and s[v] == s[u]:
                    best = max(best, down[v])
            down[u] = 1 + best
        up = [1] * n
        answer = 1
        for u in order:
            top1 = 0
            top2 = 0
            top_node = -1
            for v in graph[u]:
                if parent[v] == u and s[v] == s[u]:
                    value = down[v]
                    if value > top1:
                        top2 = top1
                        top1 = value
                        top_node = v
                    elif value > top2:
                        top2 = value
            answer = max(answer, 1 + top1 + top2)
            answer = max(answer, up[u] + top1)
            for v in graph[u]:
                if parent[v] != u:
                    continue
                if s[v] == s[u]:
                    sibling = top2 if v == top_node else top1
                    up[v] = 1 + max(up[u], 1 + sibling)
                else:
                    up[v] = 1
        best = [0] * n
        for i in range(n):
            best[i] = max(down[i], up[i])
        for u, v in edges:
            u -= 1
            v -= 1
            if s[u] != s[v]:
                answer = max(answer, best[u] + best[v])
        return answer
