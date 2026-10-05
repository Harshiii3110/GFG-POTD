class Solution:
    def socialNetwork(self, arr):
        # code here
        n = len(arr) + 1
        ans = []
        for i in range(2, n + 1):
            current = i
            distance = 0
            reachable = {}
            while current != 1:
                current = arr[current - 2]
                distance += 1
                reachable[current] = distance
            # j must be in increasing order
            for j in range(1, i):
                if j in reachable:
                    ans.append([i, j, reachable[j]])
        return ans
