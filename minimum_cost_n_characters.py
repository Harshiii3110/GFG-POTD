import heapq
class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        # code here
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0
        for x in range(1, n + 1):
            # Insert one character
            dp[x] = dp[x - 1] + i
            if x % 2 == 0:
                # Copy-paste from x/2
                dp[x] = min(
                    dp[x],
                    dp[x // 2] + c
                )
            else:
                # Option 1:
                # Copy x//2 characters to get x-1,
                # then insert one character.
                dp[x] = min(
                    dp[x],
                    dp[x // 2] + c + i
                )
                # Option 2:
                # Copy (x+1)//2 characters to get x+1,
                # then delete one character.
                dp[x] = min(
                    dp[x],
                    dp[(x + 1) // 2] + c + d
                )
        return dp[n]
