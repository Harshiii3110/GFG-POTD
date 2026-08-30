class Solution:

    def getMarks(self, l, r, rank):
        """code here"""
        queries = [(rank[i], i) for i in range(len(rank))]
        queries.sort()
        ans = [0] * len(rank)
        interval = 0
        count_before = 0
        for k, idx in queries:
            # Move to the interval containing rank k
            while interval < len(l):
                interval_count = r[interval] - l[interval] + 1
                if k <= count_before + interval_count:
                    break
                count_before += interval_count
                interval += 1
            # k lies inside current interval
            offset = k - count_before
            ans[idx] = l[interval] + offset - 1
        return ans
