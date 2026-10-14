class Solution:
    def findRollOut(self, s, roll):
        # code here
        n = len(s)
        diff = [0] * (n + 1)
        for r in roll:
            diff[0] += 1
            diff[r] -= 1
        result = []
        shifts = 0
        for i in range(n):
            shifts += diff[i]
            value = (ord(s[i]) - ord('a') + shifts) % 26
            result.append(chr(value + ord('a')))
        return ''.join(result)
