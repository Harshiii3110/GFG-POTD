class Solution:
    def minimumCost(self, cost, w):
        # code here
        INF = float('inf')
        dp = [INF] * (w + 1)
        dp[0] = 0
        n = len(cost)
        for i in range(n):
            if cost[i] == -1:
                continue
            weight = i + 1
            for j in range(weight, w + 1):
                dp[j] = min(dp[j],
                            dp[j - weight] + cost[i])
        if dp[w] == INF:
            return -1
        return dp[w]        
