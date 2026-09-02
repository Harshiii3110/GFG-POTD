class Solution:
    def solve(self, n, s):
        # code here
        status = [0] * 26
        available = n
        rejected = 0
        for ch in s:
            idx = ord(ch) - ord('A')
            if status[idx] == 0:
                # Customer arrives
                if available > 0:
                    status[idx] = 1
                    available -= 1
                else:
                    status[idx] = 2
                    rejected += 1
            elif status[idx] == 1:
                # Customer leaves after using a computer
                status[idx] = 0
                available += 1
            else:
                # Customer was rejected earlier
                # They leave, but no computer becomes free
                status[idx] = 0
        return rejected
