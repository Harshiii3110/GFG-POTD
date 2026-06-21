class Solution:
    def chooseSwap(self, s):
        # code here
        chars = set(s)
        for i in range(len(s)):
            chars.discard(s[i])
            for ch in sorted(chars):
                if ch < s[i]:
                    a = s[i]
                    b = ch
                    res = []
                    for c in s:
                        if c == a:
                            res.append(b)
                        elif c == b:
                            res.append(a)
                        else:
                            res.append(c)
                    return "".join(res)
        return s       
