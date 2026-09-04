class Solution:
    def maxFruits(self, arr: list[int], m: int) -> int:
        """ code here """
        n = len(arr)
        if m >= n:
            return sum(arr)
        window_sum = sum(arr[:m])
        ans = window_sum
        for i in range(1, n):
            window_sum -= arr[i - 1]
            window_sum += arr[(i + m - 1) % n]
            ans = max(ans, window_sum)
        return ans
