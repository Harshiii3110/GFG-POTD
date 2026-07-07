class Solution:
    def largestArea(self, n, m, k, arr):
        # code here
        rows = []
        cols = []
        for r, c in arr:
            rows.append(r)
            cols.append(c)
        rows.sort()
        cols.sort()
        maxRows = 0
        prev = 0
        for r in rows:
            maxRows = max(maxRows, r - prev - 1)
            prev = r
        maxRows = max(maxRows, n - prev)
        maxCols = 0
        prev = 0
        for c in cols:
            maxCols = max(maxCols, c - prev - 1)
            prev = c
        maxCols = max(maxCols, m - prev)
        return maxRows * maxCols        
