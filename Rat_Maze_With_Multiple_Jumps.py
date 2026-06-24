class Solution:
	def shortestDist(self, mat):
		# code here
        n = len(mat)
        if n == 1:
            return [[1]]
        if mat[0][0] == 0:
            return [[-1]]
        ans = [[0] * n for _ in range(n)]
        failed = set()
        def dfs(i, j):
            if (i, j) in failed:
                return False
            if i == n - 1 and j == n - 1:
                ans[i][j] = 1
                return True
            if i >= n or j >= n or mat[i][j] == 0:
                return False
            ans[i][j] = 1
            for step in range(1, mat[i][j] + 1):
                # Right first
                if j + step < n and dfs(i, j + step):
                    return True
                # Down second
                if i + step < n and dfs(i + step, j):
                    return True
            ans[i][j] = 0
            failed.add((i, j))
            return False
        if dfs(0, 0):
            return ans
        return [[-1]]
