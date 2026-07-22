from bisect import bisect_left
class Solution:
    def minDeletions(self, arr):
        # code here
        lis = []
        for num in arr:
            idx = bisect_left(lis, num)
            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num
        return len(arr) - len(lis)        
