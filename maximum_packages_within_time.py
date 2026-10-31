class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        # code here
        k = min(totalTime, len(arr))
        
        window_sum = sum(arr[:k])
        max_packages = window_sum
        
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            max_packages = max(max_packages, window_sum)
        
        return max_packages        
