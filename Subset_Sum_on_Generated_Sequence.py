class Solution:
    def isPossible(self, arr, s, x):
        # code here 
        numbers = [s]
        total = s
        for a in arr:
            new_value = total + a
            numbers.append(new_value)
            total += new_value
        remaining = x
        for num in reversed(numbers):
            if num <= remaining:
                remaining -= num
            if remaining == 0:
                return True
        return False
