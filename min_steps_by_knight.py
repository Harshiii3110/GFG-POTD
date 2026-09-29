from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos: list[int], targetPos: list[int], n: int) -> int:
        start_r = knightPos[0] - 1
        start_c = knightPos[1] - 1
        target_r = targetPos[0] - 1
        target_c = targetPos[1] - 1

        if (start_r, start_c) == (target_r, target_c):
            return 0

        moves = [
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (1, 2), (1, -2),
            (-1, 2), (-1, -2)
        ]

        visited = [[False] * n for _ in range(n)]
        queue = deque([(start_r, start_c, 0)])
        visited[start_r][start_c] = True

        while queue:
            r, c, steps = queue.popleft()

            for dr, dc in moves:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    if nr == target_r and nc == target_c:
                        return steps + 1

                    visited[nr][nc] = True
                    queue.append((nr, nc, steps + 1))

        return -1
