from bisect import bisect_right
class Solution:
    def maxIndexDifference(self, s):
        # code here
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            pos[ord(ch) - ord('a')].append(i)
        if not pos[0]:
            return -1
        reach = {}
        # Process from z to a
        for c in range(25, -1, -1):
            if c == 25:
                for idx in pos[c]:
                    reach[idx] = idx
                continue
            nxt = pos[c + 1]
            # suffixMax[i] = maximum reachable index among nxt[i...]
            suffixMax = [0] * (len(nxt) + 1)
            for i in range(len(nxt) - 1, -1, -1):
                suffixMax[i] = max(reach[nxt[i]], suffixMax[i + 1])
            for idx in pos[c]:
                j = bisect_right(nxt, idx)
                if j == len(nxt):
                    reach[idx] = idx
                else:
                    reach[idx] = suffixMax[j]
        ans = 0
        for idx in pos[0]:
            ans = max(ans, reach[idx] - idx)
        return ans      
