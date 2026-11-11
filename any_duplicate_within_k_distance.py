class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        # code here
        last_seen = {}

        for i in range(len(arr)):
            if arr[i] in last_seen:
                if i - last_seen[arr[i]] <= k:
                    return True

            last_seen[arr[i]] = i

        return False
