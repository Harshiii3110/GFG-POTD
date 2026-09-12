class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        # code here
        NEG_INF = float('-inf')
        POS_INF = float('inf')
        max_dp = [NEG_INF] * (k + 1)
        min_dp = [POS_INF] * (k + 1)
        max_dp[0] = 1
        min_dp[0] = 1
        for x in arr:
            for j in range(k, 0, -1):
                if max_dp[j - 1] != NEG_INF:
                    max_dp[j] = max(
                        max_dp[j],
                        max_dp[j - 1] * x,
                        min_dp[j - 1] * x
                    )
                if min_dp[j - 1] != POS_INF:
                    min_dp[j] = min(
                        min_dp[j],
                        max_dp[j - 1] * x,
                        min_dp[j - 1] * x
                    )
        return max_dp[k]
