class Solution:
    def minSquares(self, n, m):
        # code here
        count = 0
        while n > 0 and m > 0:
            if n > m:
                count += n // m
                n %= m
            else:
                count += m // n
                m %= n
        return count
