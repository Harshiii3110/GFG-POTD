class Solution:
    def minInsAndDel(self, a, b):
        # code here
        pos = {}
        for i in range(len(b)):
            pos[b[i]] = i
        arr = []
        for x in a:
            if x in pos:
                arr.append(pos[x])
        lis = []
        for x in arr:
            left = 0
            right = len(lis)
            while left < right:
                mid = (left + right) // 2
                if lis[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            if left == len(lis):
                lis.append(x)
            else:
                lis[left] = x
        lcs = len(lis)
        return len(a) + len(b) - 2 * lcs       
