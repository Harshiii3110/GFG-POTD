class Solution:
    def countSubsequences(self, s, n):
        # code here
        MOD = 1000000007
        # dp[r] = number of non-empty subsequences
        # whose value % n == r
        dp = [0] * n
        for ch in s:
            digit = int(ch)
            # Copy the old states because each character
            # can either be taken or not taken.
            new_dp = dp[:]
            # Start a new subsequence using only this digit
            new_dp[digit % n] = (new_dp[digit % n] + 1) % MOD
            # Append current digit to every existing subsequence
            for r in range(n):
                if dp[r]:
                    new_r = (r * 10 + digit) % n
                    new_dp[new_r] = (new_dp[new_r] + dp[r]) % MOD
            dp = new_dp
        return dp[0]
