class Solution:
    def getMaxWeight(self, s):
        # code here
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

            if i >= 2:
                pair_weight = 4 if s[i - 2] != s[i - 1] else 3
                dp[i] = max(dp[i], dp[i - 2] + pair_weight)

        return dp[n]
