class Solution:
    def count(self, n: int, m: int) -> int:
        # code here
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for j in range(1, m + 1):
            dp[1][j] = 1
        for i in range(2, n + 1):
            for j in range(1, m + 1):
                for k in range(1, m + 1):
                    if j % k == 0 or k % j == 0:
                        dp[i][j] += dp[i - 1][k]
        return sum(dp[n][1:])        
