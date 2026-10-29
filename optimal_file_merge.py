import heapq
class Solution:
    def minComputation(self, files):
        # code here
        heapq.heapify(files)
        total_cost = 0

        while len(files) > 1:
            first = heapq.heappop(files)
            second = heapq.heappop(files)

            merged = first + second
            total_cost += merged

            heapq.heappush(files, merged)

        return total_cost
