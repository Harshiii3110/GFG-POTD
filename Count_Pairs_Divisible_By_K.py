class Solution:
    def countKdivPairs(self, arr, k):
        # code here
        freq = [0] * k
        ans = 0
        for num in arr:
            rem = num % k
            need = (k - rem) % k
            ans += freq[need]
            freq[rem] += 1
        return ans        
