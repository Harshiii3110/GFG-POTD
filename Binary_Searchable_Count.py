class Solution:
    def binarySearchable(self, arr):
        # code here 
        n = len(arr)
        count = 0
        for i in range(n):
            l = 0
            r = n - 1
            found = False
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == arr[i]:
                    found = True
                    break
                elif arr[mid] < arr[i]:
                    l = mid + 1
                else:
                    r = mid - 1
            if found:
                count += 1
        return count
