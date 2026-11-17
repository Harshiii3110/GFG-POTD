class Solution:
    def findPattern(self, s):
        # code here
        n = len(s)
        i = 0

        while i < n:
            if s[i] != 'x':
                return False

            x_count = 0
            y_count = 0

            while i < n and s[i] == 'x':
                x_count += 1
                i += 1

            while i < n and s[i] == 'y':
                y_count += 1
                i += 1

            if x_count != y_count:
                return False

        return True
