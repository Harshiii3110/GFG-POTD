class Solution:
    def getCount (self, s, k):
        # code here
        groups = {}

        for i in range(len(s)):
            if i == 0 or s[i] != s[i - 1]:
                groups[s[i]] = groups.get(s[i], 0) + 1

        count = 0

        for char in groups:
            if groups[char] == k:
                count += 1

        return count
