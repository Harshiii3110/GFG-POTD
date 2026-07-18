class Solution {
    static final int MOD = 1000000007;

    public int findWays(int[][] matrix, int k) {
        int n = matrix.length, m = matrix[0].length;
        int[][] pre = new int[n + 1][m + 1];
        for (int i = n - 1; i >= 0; i--)
            for (int j = m - 1; j >= 0; j--)
                pre[i][j] = matrix[i][j] + pre[i + 1][j] + pre[i][j + 1] - pre[i + 1][j + 1];

        if (pre[0][0] < k) return 0;
        if (k == 1) return pre[0][0] > 0 ? 1 : 0;

        // nextDiffRow[r][c] = smallest r' in (r, n] with pre[r'][c] != pre[r][c]
        int[][] nextDiffRow = new int[n][m];
        for (int c = 0; c < m; c++)
            for (int r = n - 1; r >= 0; r--)
                nextDiffRow[r][c] = (r == n - 1 || pre[r][c] != pre[r + 1][c]) ? r + 1 : nextDiffRow[r + 1][c];

        // nextDiffCol[r][c] = smallest c' in (c, m] with pre[r][c'] != pre[r][c]
        int[][] nextDiffCol = new int[n][m];
        for (int r = 0; r < n; r++)
            for (int c = m - 1; c >= 0; c--)
                nextDiffCol[r][c] = (c == m - 1 || pre[r][c] != pre[r][c + 1]) ? c + 1 : nextDiffCol[r][c + 1];

        int[][] dpPrev = new int[n][m]; // pieces = 1
        for (int r = 0; r < n; r++)
            for (int c = 0; c < m; c++)
                dpPrev[r][c] = pre[r][c] > 0 ? 1 : 0;

        int[][] rowSuffix = new int[n + 1][m];
        int[][] colSuffix = new int[n][m + 1];
        int[][] dpCur = new int[n][m];

        for (int p = 2; p <= k; p++) {
            for (int c = 0; c < m; c++) {
                rowSuffix[n][c] = 0;
                for (int r = n - 1; r >= 0; r--) {
                    int v = dpPrev[r][c] + rowSuffix[r + 1][c];
                    rowSuffix[r][c] = v >= MOD ? v - MOD : v;
                }
            }
            for (int r = 0; r < n; r++) {
                colSuffix[r][m] = 0;
                for (int c = m - 1; c >= 0; c--) {
                    int v = dpPrev[r][c] + colSuffix[r][c + 1];
                    colSuffix[r][c] = v >= MOD ? v - MOD : v;
                }
            }

            for (int r = 0; r < n; r++) {
                for (int c = 0; c < m; c++) {
                    if (pre[r][c] < p) {
                        dpCur[r][c] = 0;
                        continue;
                    }
                    long val = rowSuffix[nextDiffRow[r][c]][c] + colSuffix[r][nextDiffCol[r][c]];
                    if (val >= MOD) val -= MOD;
                    dpCur[r][c] = (int) val;
                }
            }

            int[][] tmp = dpPrev;
            dpPrev = dpCur;
            dpCur = tmp;
        }

        return dpPrev[0][0];
    }
}
