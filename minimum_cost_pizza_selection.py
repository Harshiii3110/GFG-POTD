class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        # code here
        INF = 10**18
        dp = [INF] * (x + 1)
        dp[0] = 0
        pizzas = [
            (s, cs),
            (m, cm),
            (l, cl)
        ]
        for area in range(x + 1):
            if dp[area] == INF:
                continue
            for size, cost in pizzas:
                new_area = min(x, area + size)
                dp[new_area] = min(dp[new_area], dp[area] + cost)
        return dp[x]
