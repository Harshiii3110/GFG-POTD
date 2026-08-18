class Solution:
    def compress(self, s):
        # code here
        n = len(s)
    
        # Build LPS array
        lps = [0] * n
    
        for i in range(1, n):
            j = lps[i - 1]
    
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
    
            if s[i] == s[j]:
                j += 1
    
            lps[i] = j
    
        # Build compressed string from right to left
        ans = []
        i = n - 1
    
        while i >= 0:
            if i % 2 == 1:
                length = i + 1
                border = lps[i]
    
                if (border >= length / 2 and
                    length % (2 * (length - border)) == 0):
    
                    ans.append('*')
                    i = i // 2 + 1
                    i -= 1
                    continue
    
            ans.append(s[i])
            i -= 1
    
        return ''.join(reversed(ans))
