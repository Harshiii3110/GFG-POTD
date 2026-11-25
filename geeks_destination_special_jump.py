class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        # code here
        MOD = 10**9 + 7
        c = a - b
        def prefix_cycles(x):
            if x <= a:
                return 0
            y = x - a
            m, rem = divmod(y, c)
            return c * m * (m + 1) // 2 + rem * (m + 1)
        A = d - r
        B = d - l
        count = B - A + 1
        # Sum of all positions
        position_sum = (A + B) * count // 2
        # Sum of cycle counts
        cycle_sum = prefix_cycles(B) - prefix_cycles(A - 1)
        # Total minimum time
        answer = position_sum + count + 2 * b * cycle_sum
        return answer % MOD
