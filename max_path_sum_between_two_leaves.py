'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:        
    def maxPathSum(self, root):
        # code here
        self.ans = float('-inf')
        self.leaves = 0
        def dfs(node):
            if node is None:
                return 0
            # Leaf node
            if node.left is None and node.right is None:
                self.leaves += 1
                return node.data
            left = dfs(node.left) if node.left else float('-inf')
            right = dfs(node.right) if node.right else float('-inf')
            # A path between two leaves can pass through this node
            if node.left is not None and node.right is not None:
                self.ans = max(
                    self.ans,
                    left + node.data + right
                )
            # Return the best leaf-to-node path
            if node.left is None:
                return node.data + right
            if node.right is None:
                return node.data + left
            return node.data + max(left, right)
        dfs(root)
        if self.leaves < 2:
            return -1
        return self.ans
