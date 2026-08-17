class Solution:
    def minThrows(self, n, lad, sn):
        # code here
        destination = n * n
        jump = {}
        for i in range(0, len(lad), 2):
            jump[lad[i]] = lad[i + 1]
        for i in range(0, len(sn), 2):
            jump[sn[i]] = sn[i + 1]
        visited = [False] * (destination + 1)
        queue = deque([(1, 0)])
        visited[1] = True
        while queue:
            cell, throws = queue.popleft()
            if cell == destination:
                return throws
            for dice in range(1, 7):
                next_cell = cell + dice
                if next_cell > destination:
                    continue
                if next_cell in jump:
                    next_cell = jump[next_cell]
                if not visited[next_cell]:
                    visited[next_cell] = True
                    queue.append((next_cell, throws + 1))
        return -1   
