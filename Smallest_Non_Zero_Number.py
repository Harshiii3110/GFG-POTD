class Solution:
    def find(self, arr):
        # code here
        need = 0
        for num in reversed(arr):
            need = (need + num + 1) // 2
        return need        
        
