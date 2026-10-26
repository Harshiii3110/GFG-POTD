class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        # code here
        n = len(arr)

        if k == 0:
            return max(arr) - min(arr)

        prefix_min = [0] * n
        prefix_max = [0] * n
        suffix_min = [0] * n
        suffix_max = [0] * n

        prefix_min[0] = prefix_max[0] = arr[0]

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], arr[i])
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        suffix_min[-1] = suffix_max[-1] = arr[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])
            suffix_max[i] = max(suffix_max[i + 1], arr[i])

        answer = float('inf')

        for start in range(n - k + 1):
            end = start + k - 1

            if start == 0:
                mn = suffix_min[end + 1]
                mx = suffix_max[end + 1]
            elif end == n - 1:
                mn = prefix_min[start - 1]
                mx = prefix_max[start - 1]
            else:
                mn = min(prefix_min[start - 1], suffix_min[end + 1])
                mx = max(prefix_max[start - 1], suffix_max[end + 1])

            answer = min(answer, mx - mn)

        return answer
