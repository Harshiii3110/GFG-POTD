class Solution:
    def largestSubsquare(self, mat):
        # code here
        n = len(mat)
        right = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]
        # Precompute consecutive X's to the right and downward
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 'X':
                    right[i][j] = 1
                    down[i][j] = 1
                    if j + 1 < n:
                        right[i][j] += right[i][j + 1]
                    if i + 1 < n:
                        down[i][j] += down[i + 1][j]
        ans = 0
        # Check possible top-left corners
        for i in range(n):
            for j in range(n):
                # Maximum possible size from this top-left corner
                max_size = min(right[i][j], down[i][j])
                # No need to check sizes that cannot improve the answer
                for size in range(max_size, ans, -1):
                    bottom = i + size - 1
                    right_col = j + size - 1
                    if bottom >= n or right_col >= n:
                        continue
                    # Check bottom and right boundaries
                    if (right[bottom][j] >= size and
                        down[i][right_col] >= size):
                        ans = size
                        break
        return ans
