class Solution:
    def increasingNumbers(self, n):
        # code here
        if n == 1:
            return [i for i in range(10)]
        if n > 10:
            return []
        ans = []
        def backtrack(start, num):
            if len(num) == n:
                ans.append(int(num))
                return
            for digit in range(start, 10):
                backtrack(digit + 1, num + str(digit))
        for first in range(1, 10):
            backtrack(first + 1, str(first))
        return ans
