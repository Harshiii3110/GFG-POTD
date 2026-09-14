from collections import deque
class Solution:
    def shortestPath(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        # Mark unsafe cells
        unsafe = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    unsafe[i][j] = True
                    for dr, dc in directions:
                        ni = i + dr
                        nj = j + dc
                        if 0 <= ni < n and 0 <= nj < m:
                            unsafe[ni][nj] = True
        # Multi-source BFS
        q = deque()
        dist = [[-1] * m for _ in range(n)]
        # Start from every safe cell in first column
        for i in range(n):
            if not unsafe[i][0]:
                q.append((i, 0))
                dist[i][0] = 1
        while q:
            r, c = q.popleft()
            # Last column reached
            if c == m - 1:
                return dist[r][c]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < n and
                    0 <= nc < m and
                    not unsafe[nr][nc] and
                    dist[nr][nc] == -1):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        return -1
