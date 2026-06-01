class Solution:
    def findMaxProduct(self, arr):
        MOD = 1000000007
        if len(arr) == 1:
            return arr[0]
        product = 1
        negatives = []
        zeros = 0
        for num in arr:
            if num == 0:
                zeros += 1
            else:
                product *= num
                if num < 0:
                    negatives.append(num)
        if zeros == len(arr):
            return 0
        if len(negatives) % 2 != 0:
            largest_negative = max(negatives)
            if len(negatives) == 1 and zeros + 1 == len(arr):
                return 0
            product = product // largest_negative
        return product % MOD
