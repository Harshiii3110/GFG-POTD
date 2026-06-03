class Solution:
    def freqInRange(self, arr, queries):
        # code here
        positions = {}
        for i in range(len(arr)):
            if arr[i] not in positions:
                positions[arr[i]] = []
            positions[arr[i]].append(i)
        ans = []
        for query in queries:
            l = query[0]
            r = query[1]
            x = query[2]
            if x not in positions:
                ans.append(0)
                continue
            count = 0
            for index in positions[x]:
                if l <= index <= r:
                    count += 1
            ans.append(count)
        return ans        
