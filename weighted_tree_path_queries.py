
class Solution:
    def countPaths(self, n, edges, queries):
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            ru = find(u)
            rv = find(v)

            if ru == rv:
                return 0

            if size[ru] < size[rv]:
                ru, rv = rv, ru

            new_paths = size[ru] * size[rv]

            parent[rv] = ru
            size[ru] += size[rv]

            return new_paths

        edges.sort(key=lambda x: x[2])

        sorted_queries = sorted(
            [(queries[i], i) for i in range(len(queries))]
        )

        ans = [0] * len(queries)
        edge_index = 0
        total_paths = 0

        for weight, idx in sorted_queries:

            while (edge_index < len(edges) and
                   edges[edge_index][2] <= weight):

                u, v, w = edges[edge_index]

                total_paths += union(u, v)
                edge_index += 1

            ans[idx] = total_paths

        return ans
