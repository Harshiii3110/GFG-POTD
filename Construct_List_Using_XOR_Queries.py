class Solution:
    def constructList(self, queries):
        # code here
        arr = [0]
        xor_value = 0
        for query in queries:
            t = query[0]
            x = query[1]
            if t == 0:
                arr.append(x ^ xor_value)
            else:
                xor_value ^= x
        result = []
        for num in arr:
            result.append(num ^ xor_value)
        result.sort()
        return result
        
