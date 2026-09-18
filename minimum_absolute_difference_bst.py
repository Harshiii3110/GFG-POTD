'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''

class Solution:
    def absDiff(self, root):
        # code here
        stack = []
        current = root
        prev = None
        ans = float('inf')
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if prev is not None:
                ans = min(ans, current.data - prev)
            prev = current.data
            current = current.right
        return ans
