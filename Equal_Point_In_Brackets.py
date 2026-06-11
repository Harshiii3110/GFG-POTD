class Solution:
    def findIndex(self, s):
        close_count = s.count(')')
        open_count = 0
        for i in range(len(s)):
            if open_count == close_count:
                return i
            if s[i] == '(':
                open_count += 1
            else:
                close_count -= 1
        return len(s)
