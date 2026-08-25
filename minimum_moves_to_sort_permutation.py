class Solution:
    def minMoves(self, arr):
        """code here"""
        n = len(arr)
        pos = [0] * (n + 1)
        for i in range(n):
            pos[arr[i]] = i
        longest = 1
        current = 1
        for x in range(2, n + 1):
            if pos[x] > pos[x - 1]:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return n - longest
