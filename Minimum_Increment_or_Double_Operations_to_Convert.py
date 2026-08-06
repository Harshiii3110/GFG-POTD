class Solution:
    def countMinOperations(self, arr):
        # code here
        ans = 0
        while True:
            done = True
            for i in range(len(arr)):
                if arr[i] % 2 == 1:
                    arr[i] -= 1
                    ans += 1
                if arr[i] != 0:
                    done = False
            if done:
                break
            for i in range(len(arr)):
                arr[i] //= 2
            ans += 1
        return ans
