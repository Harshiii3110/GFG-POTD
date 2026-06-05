class Solution:
    def lexicographicallySmallest(self, s, k):
        # code here 
        n = len(s)
        if (n & (n - 1)) == 0:
            k = k // 2
        else:
            k = k * 2
        if k >= n:
            return -1
        stack = []
        for ch in s:
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        while k > 0:
            stack.pop()
            k -= 1
        ans = "".join(stack)
        if ans == "":
            return -1
        return ans        
