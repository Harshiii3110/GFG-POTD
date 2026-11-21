class Solution:
    def smallestSubWithSum(self, arr, x):
        # code here 
        n = len(arr)
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(n):
            current_sum += arr[right]

            while current_sum > x:
                min_length = min(min_length, right - left + 1)
                current_sum -= arr[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length
