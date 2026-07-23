class Solution:
    def canRepresentBST(self, arr):
        # code here
        stack = []
        root = float('-inf')
        for value in arr:
            if value < root:
                return False
            while stack and value > stack[-1]:
                root = stack.pop()
            stack.append(value)
        return True        
