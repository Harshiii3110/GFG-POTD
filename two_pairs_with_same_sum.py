class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        # code here
        n = len(arr)
        groups = {}

        # Generate all pairs in lexicographical order
        for i in range(n):
            for j in range(i + 1, n):
                total = arr[i] + arr[j]

                if total not in groups:
                    groups[total] = []

                groups[total].append((i, j))

        answer = None

        # Process pairs having the same sum
        for pairs in groups.values():
            if len(pairs) < 2:
                continue

            # Count how many pairs contain each index
            degree = {}

            for a, b in pairs:
                degree[a] = degree.get(a, 0) + 1
                degree[b] = degree.get(b, 0) + 1

            remaining = len(pairs)

            for i in range(len(pairs)):
                a, b = pairs[i]

                # Remove the current pair from remaining pairs
                remaining -= 1
                degree[a] -= 1
                degree[b] -= 1

                # Count remaining pairs disjoint from (a, b)
                disjoint = remaining - degree[a] - degree[b]

                if disjoint > 0:
                    # Find the earliest disjoint partner
                    for j in range(i + 1, len(pairs)):
                        c, d = pairs[j]

                        if a != c and a != d and b != c and b != d:
                            candidate = (a, b, c, d)

                            if answer is None or candidate < answer:
                                answer = candidate

                            break

                    # First valid pair is lexicographically smallest
                    break

        if answer is None:
            return [-1, -1, -1, -1]

        return list(answer)
