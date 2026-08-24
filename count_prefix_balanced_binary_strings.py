class Solution:
    def prefixStrings(self, n: int) -> int:
        # code here
        MOD = 10**9 + 7
        # Calculate C(2n, n)
        numerator = 1
        denominator = 1
        for i in range(1, n + 1):
            numerator = numerator * (n + i) % MOD
            denominator = denominator * i % MOD
        # Modular inverse of denominator
        comb = numerator * pow(denominator, MOD - 2, MOD) % MOD
        # Catalan number = C(2n,n) / (n+1)
        ans = comb * pow(n + 1, MOD - 2, MOD) % MOD
        return ans
