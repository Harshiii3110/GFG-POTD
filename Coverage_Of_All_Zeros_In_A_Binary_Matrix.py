class Solution:
    def findCoverage(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        total = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    coverage = 0
                    # Left
                    col = j - 1
                    while col >= 0:
                        if mat[i][col] == 1:
                            coverage += 1
                            break
                        col -= 1
                    # Right
                    col = j + 1
                    while col < m:
                        if mat[i][col] == 1:
                            coverage += 1
                            break
                        col += 1
                    # Up
                    row = i - 1
                    while row >= 0:
                        if mat[row][j] == 1:
                            coverage += 1
                            break
                        row -= 1
                    # Down
                    row = i + 1
                    while row < n:
                        if mat[row][j] == 1:
                            coverage += 1
                            break
                        row += 1
                    total += coverage
        return total        
