class Solution:
    def findMax(self, n, a, b, k):
        # code here
        diff = [0] * (n + 1)
        for i in range(len(a)):
            diff[a[i]] += k[i]
            if b[i] + 1 < n:
                diff[b[i] + 1] -= k[i]
        ans = 0
        curr = 0
        for i in range(n):
            curr += diff[i]
            ans = max(ans, curr)
        return ans        
