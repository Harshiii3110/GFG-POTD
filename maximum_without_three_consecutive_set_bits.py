class Solution:

    def maxValue(self, n: int) -> int:
        """code here"""
        while True:
            binary = bin(n)[2:]
            index = binary.find("111")
            if index == -1:
                return n
            binary = binary[:index + 2] + "0" + binary[index + 3:]
            n = int(binary, 2)
