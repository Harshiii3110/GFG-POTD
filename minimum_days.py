class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        # code here
        n = len(s)

        def isValid(days):
            removed = [False] * n

            for i in range(days):
                removed[p[i]] = True

            for i in range(n - 1):
                if not removed[i] and not removed[i + 1]:
                    if s[i] == s[i + 1]:
                        return False

            return True

        if isValid(0):
            return 0

        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if isValid(mid):
                right = mid
            else:
                left = mid + 1

        return left
