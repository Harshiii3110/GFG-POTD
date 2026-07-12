class Solution:
    def maxAmount(self, arr, k):
        # code here
        MOD = 1000000007
        heap = []
        for x in arr:
            heapq.heappush(heap, -x)
        ans = 0
        while k > 0 and heap:
            val = -heapq.heappop(heap)
            ans = (ans + val) % MOD
            if val > 1:
                heapq.heappush(heap, -(val - 1))
            k -= 1
        return ans        
