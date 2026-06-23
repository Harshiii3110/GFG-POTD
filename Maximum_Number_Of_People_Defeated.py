class Solution:
    def maxPeopleDefeated(self, p):
        # code here        
        left = 0
        right = 10000
        while left <= right:
            mid = (left + right) // 2
            total = mid * (mid + 1) * (2 * mid + 1) // 6
            if total <= p:
                left = mid + 1
            else:
                right = mid - 1
        return right
        
