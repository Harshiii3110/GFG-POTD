class Solution:
    def computeValue(self, n):
        # code here
        MOD = 10**9 + 7
        fact = [1] * (2 * n + 1)
        for i in range(1, 2 * n + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        numerator = fact[2 * n]
        denominator = (fact[n] * fact[n]) % MOD
        inverse = pow(denominator, MOD - 2, MOD)
        return (numerator * inverse) % MOD        
