'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = self.left = None
        
'''

class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        # code here
        minimum = float('inf')
        current = root

        while current:
            difference = abs(current.data - k)
            minimum = min(minimum, difference)

            if difference == 0:
                return 0

            if k < current.data:
                current = current.left
            else:
                current = current.right

        return minimum
