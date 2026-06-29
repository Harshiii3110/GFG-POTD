class Solution:
    def maxDotProduct(self, a, b):
        # code here
        n = len(a)
        m = len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            limit = min(i, m)
            for j in range(1, limit + 1):
                if i == j:
                    dp[i][j] = dp[i - 1][j - 1] + a[i - 1] * b[j - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i - 1][j - 1] + a[i - 1] * b[j - 1]
                    )
        return dp[n][m]        
