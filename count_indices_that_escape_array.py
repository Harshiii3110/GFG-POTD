class Solution:
    def goodIndices(self, arr):
        # code here
        n = len(arr)
        state = [0] * n  # 0 = unknown, 1 = good, -1 = bad, 2 = visiting

        for start in range(n):
            if state[start] != 0:
                continue

            path = []
            pos = start

            while 0 <= pos < n and state[pos] == 0:
                state[pos] = 2
                path.append(pos)
                pos += arr[pos]

            if pos < 0 or pos >= n or state[pos] == 1:
                result = 1
            else:
                result = -1

            for idx in reversed(path):
                state[idx] = result

        return state.count(1)
