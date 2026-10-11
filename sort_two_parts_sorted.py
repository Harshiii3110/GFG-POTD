class Solution:
    def mergeTwoParts(self, arr):
        # code here
        n = len(arr)
        break_point = n
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                break_point = i
                break
        left = arr[:break_point]
        right = arr[break_point:]
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr
