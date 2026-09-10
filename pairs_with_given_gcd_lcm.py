class Solution:

    def pairCount(self, x, y):
        """code here"""
        if y % x != 0:
            return 0
        n = y // x
        distinct = 0
        p = 2
        while p * p <= n:
            if n % p == 0:
                distinct += 1
                while n % p == 0:
                    n //= p
            p += 1
        if n > 1:
            distinct += 1
        return 1 << distinct
