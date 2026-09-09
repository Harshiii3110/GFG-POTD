class Solution:
    def findMax(self, n):
        # code here
        s = str(n)
        best = n
        best_sum = sum(int(c) for c in s)
        for i in range(len(s)):
            if s[i] == '0':
                continue
            candidate = int(
                s[:i] +
                str(int(s[i]) - 1) +
                '9' * (len(s) - i - 1)
            )
            current_sum = sum(int(c) for c in str(candidate))
            if current_sum > best_sum:
                best = candidate
                best_sum = current_sum
            elif current_sum == best_sum:
                best = max(best, candidate)
        return best
