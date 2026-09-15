''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def getCount(self, root, k):
        # code here
        if not root:
            return 0
        q = deque([(root, 1)])
        leaf_costs = []
        while q:
            node, level = q.popleft()
            # Leaf node
            if node.left is None and node.right is None:
                leaf_costs.append(level)
                continue
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        # Visit cheapest leaves first
        leaf_costs.sort()
        count = 0
        for cost in leaf_costs:
            if cost > k:
                break
            k -= cost
            count += 1
        return count
