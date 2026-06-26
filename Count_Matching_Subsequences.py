class Solution:
    def countWays(self, s1, s2):
        # code here
        MOD = 1000000007
        n = len(s2)
        dp = [0] * (n + 1)
        dp[0] = 1
        for ch1 in s1:
            for j in range(n - 1, -1, -1):
                if ch1 == s2[j]:
                    dp[j + 1] = (dp[j + 1] + dp[j]) % MOD
        return dp[n]        
