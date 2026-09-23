class Solution:
    def formPyramid(self, arr):
        # code here 
        n = len(arr)
        left = [0] * n
        right = [0] * n
        left[0] = 1
        for i in range(1, n):
            left[i] = min(arr[i], left[i - 1] + 1)
        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = min(arr[i], right[i + 1] + 1)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        best = 0
        for i in range(n):
            peak = min(left[i], right[i])
            left_len = peak - 1
            right_len = peak - 1
            left_sum = peak * (peak + 1) // 2
            right_sum = left_sum - peak
            best = max(best, left_sum + right_sum)
        return sum(arr) - best
