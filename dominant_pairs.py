class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        # code here
        n = len(arr) // 2
        left = sorted(arr[: n])
        right = sorted(arr[n:])
        j = 0
        count = 0
        for x in left:
            while j < n and 5 * right[j] <= x:
                j += 1
            count += j
        return count
