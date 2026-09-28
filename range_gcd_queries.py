from math import gcd
class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        # code here
        n = len(arr)
        tree = [0] * (4 * n)

        def build(node, start, end):
            if start == end:
                tree[node] = arr[start]
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = gcd(tree[node * 2], tree[node * 2 + 1])

        def update(node, start, end, index, value):
            if start == end:
                tree[node] = value
                return

            mid = (start + end) // 2

            if index <= mid:
                update(node * 2, start, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, end, index, value)

            tree[node] = gcd(tree[node * 2], tree[node * 2 + 1])

        def query(node, start, end, left, right):
            if right < start or end < left:
                return 0

            if left <= start and end <= right:
                return tree[node]

            mid = (start + end) // 2

            left_gcd = query(node * 2, start, mid, left, right)
            right_gcd = query(node * 2 + 1, mid + 1, end, left, right)

            return gcd(left_gcd, right_gcd)

        build(1, 0, n - 1)

        answer = []

        for query_data in queries:
            if query_data[0] == 0:
                _, left, right = query_data
                answer.append(query(1, 0, n - 1, left, right))
            else:
                _, index, value = query_data
                arr[index] = value
                update(1, 0, n - 1, index, value)

        return answer
