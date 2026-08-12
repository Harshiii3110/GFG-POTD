class Solution:
    def findWays(self, grid):
        # code here
        n = len(grid)
        MOD = 10**9 + 7
        # dp[i][j] = [number of paths, maximum adventure]
        dp = [[0] * n for _ in range(n)]
        best = [[-1] * n for _ in range(n)]
        dp[0][0] = 1
        best[0][0] = grid[0][0]
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                # From the top: previous cell must allow Down
                if i > 0 and grid[i - 1][j] in (2, 3):
                    dp[i][j] = dp[i - 1][j]
                    best[i][j] = best[i - 1][j] + grid[i][j]
                # From the left: previous cell must allow Right
                if j > 0 and grid[i][j - 1] in (1, 3):
                    paths = dp[i][j - 1]
                    value = best[i][j - 1] + grid[i][j]
                    if paths:
                        if dp[i][j] == 0:
                            dp[i][j] = paths
                            best[i][j] = value
                        else:
                            dp[i][j] = (dp[i][j] + paths) % MOD
                            best[i][j] = max(best[i][j], value)
        if dp[n - 1][n - 1] == 0:
            return [0, 0]
        return [dp[n - 1][n - 1] % MOD, best[n - 1][n - 1]]
