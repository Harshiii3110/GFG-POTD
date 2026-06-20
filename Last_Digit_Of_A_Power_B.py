class Solution:
    def getLastDigit(self, a, b):
        # code here
        if b == "0":
            return 1
        last_digit = int(a[-1])
        exponent = int(b)
        return pow(last_digit, exponent, 10)        
