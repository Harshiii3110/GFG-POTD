class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        # code here
        n = len(mat)
        m = len(mat[0])
        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1
        visited = [[False] * m for _ in range(n)]
        def dfs(x, y):
            if x == xd and y == yd:
                return 0
            visited[x][y] = True
            ans = -1
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if (0 <= nx < n and
                    0 <= ny < m and
                    mat[nx][ny] == 1 and
                    not visited[nx][ny]):
                    dist = dfs(nx, ny)
                    if dist != -1:
                        ans = max(ans, dist + 1)
            visited[x][y] = False
            return ans
        return dfs(xs, ys)        
