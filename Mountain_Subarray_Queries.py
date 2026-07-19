class Solution:
    def processQueries(self, arr, queries):
        # code here
        n = len(arr)
        inc = [0] * n
        dec = [0] * n
        inc[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                inc[i] = inc[i + 1]
            else:
                inc[i] = i
        dec[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                dec[i] = dec[i + 1]
            else:
                dec[i] = i
        ans = []
        for l, r in queries:
            peak = inc[l]
            if dec[peak] >= r:
                ans.append(True)
            else:
                ans.append(False)
        return ans        
