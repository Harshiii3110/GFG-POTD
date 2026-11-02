class Solution:
    def largestSumCycle(self, edge):
        # code here
        n = len(edge)
        visited = [False] * n
        max_sum = -1

        for start in range(n):
            if visited[start]:
                continue

            path = []
            position = {}
            node = start

            while node != -1 and not visited[node]:
                visited[node] = True
                position[node] = len(path)
                path.append(node)

                node = edge[node]

            # Check whether a cycle exists in the current path
            if node in position:
                cycle_start = position[node]
                cycle_sum = sum(path[cycle_start:])
                max_sum = max(max_sum, cycle_sum)

        return max_sum
