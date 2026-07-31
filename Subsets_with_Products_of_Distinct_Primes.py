class Solution:
    def countSubsets(self, arr):
        # code here
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        freq = [0] * 31
        for x in arr:
            freq[x] += 1
        masks = [-1] * 31
        for num in range(2, 31):
            x = num
            mask = 0
            ok = True
            for i, p in enumerate(primes):
                if x % (p * p) == 0:
                    ok = False
                    break
                if x % p == 0:
                    mask |= 1 << i
            if ok:
                masks[num] = mask
        dp = [0] * (1 << 10)
        dp[0] = 1
        for num in range(2, 31):
            if freq[num] == 0 or masks[num] == -1:
                continue
            m = masks[num]
            for state in range((1 << 10) - 1, -1, -1):
                if (state & m) == 0:
                    dp[state | m] = (dp[state | m] + dp[state] * freq[num]) % MOD
        ans = 0
        for i in range(1, 1 << 10):
            ans = (ans + dp[i]) % MOD
        ans = ans * pow(2, freq[1], MOD) % MOD
        return ans
