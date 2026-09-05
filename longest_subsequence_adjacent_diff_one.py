class Solution:
    def longestSubseq(self, arr):
        # code here
        dp = {}
        ans = 1
        for x in arr:
            left = dp.get(x - 1, 0)
            right = dp.get(x + 1, 0)
            dp[x] = max(dp.get(x, 0), left + 1, right + 1)
            ans = max(ans, dp[x])
        return ans
