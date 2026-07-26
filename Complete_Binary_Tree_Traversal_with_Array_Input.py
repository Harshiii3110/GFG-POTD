class Solution:
    def levelSort(self, arr):
        # code here
        n = len(arr)
        ans = []
        index = 0
        level_size = 1
        while index < n:
            level = arr[index:min(index + level_size, n)]
            level.sort()
            ans.append(level)
            index += level_size
            level_size *= 2
        return ans        
