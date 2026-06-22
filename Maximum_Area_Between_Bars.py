class Solution:
    def maxArea(self, height):
        # code here
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            width = right - left - 1
            ans = max(ans, min(height[left], height[right]) * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans        
