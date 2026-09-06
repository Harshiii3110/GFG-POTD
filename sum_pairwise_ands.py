class Solution:
    def pairAndSum(self, arr):
        # code here
        n = len(arr)
        ans = 0
        for bit in range(31):
            cnt = 0
            mask = 1 << bit
            for num in arr:
                if num & mask:
                    cnt += 1
            pairs = cnt * (cnt - 1) // 2
            ans += pairs * mask
        return ans
