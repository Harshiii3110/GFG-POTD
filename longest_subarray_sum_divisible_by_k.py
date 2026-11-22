
class Solution:
    def longestSubarrayDivK(self, arr, k):
        remainder_index = {0: -1}

        prefix_sum = 0
        max_length = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            remainder = prefix_sum % k

            if remainder in remainder_index:
                length = i - remainder_index[remainder]
                max_length = max(max_length, length)
            else:
                remainder_index[remainder] = i

        return max_length
