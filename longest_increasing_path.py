class Solution:
    def longIncPath(self, matrix, n, m):
        # code here
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]
            dp[r][c] = 1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < n and
                    0 <= nc < m and
                    matrix[nr][nc] > matrix[r][c]):
                    dp[r][c] = max(
                        dp[r][c],
                        1 + dfs(nr, nc)
                    )
            return dp[r][c]
        answer = 0
        for r in range(n):
            for c in range(m):
                answer = max(answer, dfs(r, c))
        return answer
