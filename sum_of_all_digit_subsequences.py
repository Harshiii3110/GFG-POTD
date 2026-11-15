class Solution:

    def subsequenceSum(self, s):
        """code here"""
        MOD = 10**9 + 7

        digit_sum = 0

        for ch in s:
            digit_sum += int(ch)

        return (digit_sum * pow(2, len(s) - 1, MOD)) % MOD
