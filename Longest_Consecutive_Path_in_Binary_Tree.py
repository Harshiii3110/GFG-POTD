'''
Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def longestConsecutive(self, root):
        # Code here
        self.ans = 1
        def dfs(node, parent_val, length):
            if not node:
                return
            if node.data == parent_val + 1:
                length += 1
            else:
                length = 1
            self.ans = max(self.ans, length)
            dfs(node.left, node.data, length)
            dfs(node.right, node.data, length)
        dfs(root, float('-inf'), 0)
        return self.ans if self.ans >= 2 else -1
        
