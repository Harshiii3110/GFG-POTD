class Solution:
    def maxStackHeight(self, r, h):
        # code here
        n = len(r)
        discs = [(r[i], h[i]) for i in range(n)]
        discs.sort()
        bit = [0] * 1002
        def query(x):
            ans = 0
            while x > 0:
                ans = max(ans, bit[x])
                x -= x & -x
            return ans
        def update(x, value):
            while x < len(bit):
                bit[x] = max(bit[x], value)
                x += x & -x
        answer = 0
        i = 0
        while i < n:
            j = i
            while j < n and discs[j][0] == discs[i][0]:
                j += 1
            updates = []
            for k in range(i, j):
                radius, height = discs[k]
                best = query(height - 1)
                current = best + height
                answer = max(answer, current)
                updates.append((height, current))
            for height, current in updates:
                update(height, current)
            i = j
        return answer
