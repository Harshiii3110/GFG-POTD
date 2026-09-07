class Solution:
    def minCount(self, arr):
        """ code here """
        n = len(arr)
        # dp[(inc_last, dec_last)] = maximum number of
        # elements selected so far
        #
        # -1 means that the corresponding subsequence is empty.
        dp = {(-1, -1): 0}
        for k in range(n):
            new_dp = {}
            for (inc_last, dec_last), count in dp.items():
                # 1. Leave arr[k] unused
                state = (inc_last, dec_last)
                new_dp[state] = max(new_dp.get(state, 0), count)
                # 2. Put arr[k] in increasing subsequence
                if inc_last == -1 or arr[k] > arr[inc_last]:
                    state = (k, dec_last)
                    new_dp[state] = max(
                        new_dp.get(state, 0),
                        count + 1
                    )
                # 3. Put arr[k] in decreasing subsequence
                if dec_last == -1 or arr[k] < arr[dec_last]:
                    state = (inc_last, k)
                    new_dp[state] = max(
                        new_dp.get(state, 0),
                        count + 1
                    )
            dp = new_dp
        max_selected = max(dp.values())
        return n - max_selected
