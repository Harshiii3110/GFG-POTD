from collections import deque
class Solution:
    def minTime(self, duration, dependencies):
        # code here
        n = len(duration)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in dependencies:
            graph[u].append(v)
            indegree[v] += 1
        # Earliest finishing time for each module
        finish = duration[:]
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        ans = 0
        while q:
            u = q.popleft()
            count += 1
            ans = max(ans, finish[u])
            for v in graph[u]:
                finish[v] = max(finish[v], finish[u] + duration[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        # Cycle exists
        if count != n:
            return -1
        return ans
