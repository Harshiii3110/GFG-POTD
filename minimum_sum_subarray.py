class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        current_sum = arr[0]
        min_sum = arr[0]

        for i in range(1, len(arr)):
            current_sum = min(arr[i], current_sum + arr[i])
            min_sum = min(min_sum, current_sum)

        return min_sum
