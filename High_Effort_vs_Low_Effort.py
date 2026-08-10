class Solution:
    def maxTask(self, h: list[int], l: list[int]) -> int:
        # code here
        n = len(h)
        no_task = 0
        low = l[0]
        high = h[0]
        for i in range(1, n):
            new_no = max(no_task, low, high)
            new_low = max(no_task, low, high) + l[i]
            new_high = no_task + h[i]
            no_task = new_no
            low = new_low
            high = new_high
        return max(no_task, low, high)
