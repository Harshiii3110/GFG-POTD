from math import gcd
class Solution:
    def sameMod(self, arr):
        # code here
        n = len(arr)
        # If all elements are equal, infinitely many k are possible
        g = 0
        for i in range(1, n):
            g = gcd(g, abs(arr[i] - arr[0]))
        if g == 0:
            return -1
        # Count positive divisors of g
        count = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                count += 1
                if i != g // i:
                    count += 1
            i += 1
        return count
