class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        heights = [0] * m
        answer = 0
        for i in range(n):
            # Build histogram heights
            for j in range(m):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            # Columns can be swapped, so arrange heights
            # from largest to smallest
            sorted_heights = sorted(heights, reverse=True)
            # Try each possible width
            for j in range(m):
                width = j + 1
                area = sorted_heights[j] * width
                answer = max(answer, area)
        return answer
