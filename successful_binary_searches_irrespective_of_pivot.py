class Solution:
    def countAlwaysFound(self, arr):
        # code here
        n = len(arr)

        prefix_max = [0] * n
        suffix_min = [0] * n

        prefix_max[0] = arr[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        suffix_min[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])

        count = 0

        for i in range(n):
            left_ok = (i == 0 or arr[i] > prefix_max[i - 1])
            right_ok = (i == n - 1 or arr[i] < suffix_min[i + 1])

            if left_ok and right_ok:
                count += 1

        return count
        
