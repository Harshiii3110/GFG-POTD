class Solution:

    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        """ code here """
        MOD = 10**9 + 7
        n = len(arr)

        freq = [0] * (n + 1)

        for num in arr:
            freq[num] += 1

        power2 = [1] * (n + 1)

        for i in range(1, n + 1):
            power2[i] = (power2[i - 1] * 2) % MOD

        ans = 0
        required = 1
        prefix = 0

        for mex in range(r + 1):

            if mex > 0:
                required = (
                    required * (power2[freq[mex - 1]] - 1)
                ) % MOD

            prefix += freq[mex]

            ways = (required * power2[n - prefix]) % MOD

            if mex >= l:
                ans = (ans + ways) % MOD

        return ans
