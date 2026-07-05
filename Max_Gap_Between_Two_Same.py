class Solution:

    def maxCharGap(self, s: str) -> int:
        # code here
        first = {}
        ans = -1
        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i
            else:
                ans = max(ans, i - first[s[i]] - 1)
        return ans
