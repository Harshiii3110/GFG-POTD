class Solution:

    def minCost(self, mat):
        """code here"""
        n = len(mat)
        # dp[j] = minimum cost up to the current row
        # if choice j is selected
        dp = mat[0][:]
        for i in range(1, n):
            new_dp = [0] * 3
            new_dp[0] = mat[i][0] + min(dp[1], dp[2])
            new_dp[1] = mat[i][1] + min(dp[0], dp[2])
            new_dp[2] = mat[i][2] + min(dp[0], dp[1])
            dp = new_dp
        return min(dp)
