class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        # code here
        total = (n * m) * (n * m - 1)
        attack = 0
        if n > 1 and m > 2:
            attack += (n - 1) * (m - 2)
        if n > 2 and m > 1:
            attack += (n - 2) * (m - 1)
        attack *= 4
        return total - attack        
