class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        # code here
        left = 0
        right = n * min(s1, s2)

        while left < right:
            mid = left + (right - left) // 2

            documents = mid // s1 + mid // s2

            if documents >= n:
                right = mid
            else:
                left = mid + 1

        return left
