class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        # code here
        n = len(arr)
        maxEndHere = [0] * n
        maxEndHere[0] = arr[0]
        for i in range(1, n):
            maxEndHere[i] = max(arr[i], maxEndHere[i - 1] + arr[i])
        windowSum = sum(arr[:k])
        ans = windowSum
        for i in range(k, n):
            windowSum += arr[i] - arr[i - k]
            ans = max(ans, windowSum)
            ans = max(ans, windowSum + maxEndHere[i - k])
        return ans
