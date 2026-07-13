class Solution:
    def minOperations(self, b):
        # code here
        MOD = 1000000007
        n = len(b)
        visited = [False] * n
        def gcd(a, c):
            while c:
                a, c = c, a % c
            return a
        ans = 1
        for i in range(n):
            if not visited[i]:
                length = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = b[j] - 1
                    length += 1
                ans = (ans * (length // gcd(ans, length))) % MOD
        return ans                
