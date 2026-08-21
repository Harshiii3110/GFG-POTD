class Solution:
    def transform(self, s1, s2): 
        #code here
        if len(s1) != len(s2):
            return -1
        # Check whether transformation is possible
        if sorted(s1) != sorted(s2):
            return -1
        i = len(s1) - 1
        j = len(s2) - 1
        # Find the longest suffix of s1
        # that is also a suffix of s2
        while i >= 0:
            if s1[i] == s2[j]:
                j -= 1
                if j < 0:
                    break
            i -= 1
        return j + 1
