class Solution:
    def optimalArray(self, arr):
        # code here
        n = len(arr)
        ans = []
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        for i in range(n):
            mid = i // 2
            median = arr[mid]
            left_count = mid
            left_sum = prefix[mid]
            left_cost = median * left_count - left_sum
            right_count = i - mid
            right_sum = prefix[i + 1] - prefix[mid + 1]
            right_cost = right_sum - median * right_count
            ans.append(left_cost + right_cost)
        return ans        
