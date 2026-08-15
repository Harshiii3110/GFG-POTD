class Solution:

    def countWithout(self, n: int, d: int) -> int:
        # code here
        from functools import lru_cache

        digits = str(n)

        @lru_cache(None)
        def dp(pos, tight, started):
            if pos == len(digits):
                return 1 if started else 0

            limit = int(digits[pos]) if tight else 9
            ans = 0

            for digit in range(limit + 1):
                new_tight = tight and (digit == limit)

                if not started and digit == 0:
                    new_started = False
                else:
                    new_started = True

                # Reject d only when this is an actual digit
                if new_started and digit == d:
                    continue

                ans += dp(pos + 1, new_tight, new_started)

            return ans

        return dp(0, True, False)
