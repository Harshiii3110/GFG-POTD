class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        # code here
        def count(limit):
            left = 0
            curr = 0
            ans = 0
            for right in range(len(arr)):
                curr += arr[right]
                while curr > limit:
                    curr -= arr[left]
                    left += 1
                ans += right - left + 1
            return ans
        return count(r) - count(l - 1)    
