class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        if mat[r][c] == '#':
            return 0
        # dist[x][y] = minimum number of upward moves
        # needed to reach (x, y).
        dist = [[float('inf')] * m for _ in range(n)]
        dist[r][c] = 0
        pq = [(0, r, c)]
        while pq:
            up, x, y = heapq.heappop(pq)
            if up != dist[x][y]:
                continue
            # Number of downward moves is determined by:
            # down = up + (x - r)
            down = up + (x - r)
            if up > u or down > d:
                continue
            # Move Up
            if x > 0 and mat[x - 1][y] == '.':
                new_up = up + 1
                if new_up <= u and new_up < dist[x - 1][y]:
                    dist[x - 1][y] = new_up
                    heapq.heappush(pq, (new_up, x - 1, y))
            # Move Down
            if x + 1 < n and mat[x + 1][y] == '.':
                new_up = up
                if new_up + (x + 1 - r) <= d and new_up < dist[x + 1][y]:
                    dist[x + 1][y] = new_up
                    heapq.heappush(pq, (new_up, x + 1, y))
            # Move Left
            if y > 0 and mat[x][y - 1] == '.':
                if up < dist[x][y - 1]:
                    dist[x][y - 1] = up
                    heapq.heappush(pq, (up, x, y - 1))
            # Move Right
            if y + 1 < m and mat[x][y + 1] == '.':
                if up < dist[x][y + 1]:
                    dist[x][y + 1] = up
                    heapq.heappush(pq, (up, x, y + 1))
        ans = 0
        for i in range(n):
            for j in range(m):
                if dist[i][j] != float('inf'):
                    up = dist[i][j]
                    down = up + (i - r)
                    if up <= u and down <= d:
                        ans += 1
        return ans
