class Solution:
    def waysToIncreaseLCSBy1(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)
        L = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
        R = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    R[i][j] = R[i + 1][j + 1] + 1
                else:
                    R[i][j] = max(R[i + 1][j], R[i][j + 1])
        lcs = L[n][m]
        ans = 0
        for i in range(n + 1):
            used = set()
            for j in range(m):
                if s2[j] in used:
                    continue
                if L[i][j] + 1 + R[i][j + 1] == lcs + 1:
                    ans += 1
                    used.add(s2[j])
        return ans        
