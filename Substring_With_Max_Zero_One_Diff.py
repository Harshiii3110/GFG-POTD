class Solution:
	def maxSubstring(self, s):
		# code here
        curr_sum = 0
        max_sum = -1
        for ch in s:
            if ch == '0':
                curr_sum += 1
            else:
                curr_sum -= 1
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum		
