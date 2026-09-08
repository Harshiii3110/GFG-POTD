class Solution:
    def searchWord(self, mat, word):
        # code here
        n = len(mat)
        m = len(mat[0])
        # 8 possible directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        result = []
        length = len(word)
        for r in range(n):
            for c in range(m):
                # First character must match
                if mat[r][c] != word[0]:
                    continue
                # Try all 8 directions
                for dr, dc in directions:
                    k = 1
                    while k < length:
                        nr = r + dr * k
                        nc = c + dc * k
                        # Outside the grid
                        if nr < 0 or nr >= n or nc < 0 or nc >= m:
                            break
                        # Character doesn't match
                        if mat[nr][nc] != word[k]:
                            break
                        k += 1
                    # Entire word matched
                    if k == length:
                        result.append([r, c])
                        break
        return result
