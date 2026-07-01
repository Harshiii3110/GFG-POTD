class Solution:
    def maxSumSubarray(self, arr):
        # code here
        n = len(arr)
        if n == 1:
            return arr[0]
        keep = arr[0]
        delete = 0
        ans = arr[0]
        for i in range(1, n):
            new_delete = max(keep, delete + arr[i])
            keep = max(arr[i], keep + arr[i])
            delete = new_delete
            ans = max(ans, keep, delete)
        return ans        
