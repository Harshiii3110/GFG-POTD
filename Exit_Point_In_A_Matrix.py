class Solution:
    def exitPoint(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        i = 0
        j = 0
        direction = 0
        while 0 <= i < n and 0 <= j < m:
            if mat[i][j] == 1:
                direction = (direction + 1) % 4
                mat[i][j] = 0
            if direction == 0:
                j += 1
            elif direction == 1:
                i += 1
            elif direction == 2:
                j -= 1
            else:
                i -= 1
        if direction == 0:
            j -= 1
        elif direction == 1:
            i -= 1
        elif direction == 2:
            j += 1
        else:
            i += 1
        return [i, j]        
