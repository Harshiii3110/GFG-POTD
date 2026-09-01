class Solution:
    def palindromicStrings(self, n, k):
        # code here
        MOD = 1000000007
        ans = 0
        for length in range(1, n + 1):
            half = length // 2
            if length % 2 == 0:
                # P(k, half)
                ways = 1
                for j in range(half):
                    ways = ways * (k - j) % MOD
                ans = (ans + ways) % MOD
            else:
                # k choices for center
                # P(k-1, half) choices for first half
                ways = 1
                for j in range(half):
                    ways = ways * (k - 1 - j) % MOD
                ans = (ans + k * ways) % MOD
        return ans
