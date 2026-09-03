class Solution:
    def maxDiffSum(self, arr):
        # code here
        n = len(arr)
        if n == 1:
            return 0
        # Current element is kept
        dp0 = 0
        # Current element is replaced by 1
        dp1 = 0
        for i in range(1, n):
            # Current element kept as arr[i]
            new_dp0 = max(
                dp0 + abs(arr[i] - arr[i - 1]),
                dp1 + abs(arr[i] - 1)
            )
            # Current element replaced by 1
            new_dp1 = max(
                dp0 + abs(1 - arr[i - 1]),
                dp1 + abs(1 - 1)
            )
            dp0 = new_dp0
            dp1 = new_dp1
        return max(dp0, dp1)
