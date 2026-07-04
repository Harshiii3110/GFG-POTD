class Solution:
    def countSubstring(self, s):
        # code here
        prefix = [0]
        cur = 0
        for ch in s:
            if ch == '1':
                cur += 1
            else:
                cur -= 1
            prefix.append(cur)
        vals = sorted(set(prefix))
        comp = {}
        for i in range(len(vals)):
            comp[vals[i]] = i + 1
        bit = [0] * (len(vals) + 2)
        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i
        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res
        ans = 0
        for x in prefix:
            idx = comp[x]
            ans += query(idx - 1)
            update(idx)
        return ans
