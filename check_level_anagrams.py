"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""

from collections import deque, Counter
class Solution:

    def areAnagrams(self, root1, root2):
        """ code here """
        q1 = deque([root1])
        q2 = deque([root2])
        while q1 and q2:
            size1 = len(q1)
            size2 = len(q2)
            level1 = []
            level2 = []
            for _ in range(size1):
                node = q1.popleft()
                if node:
                    level1.append(node.data)
                    if node.left:
                        q1.append(node.left)
                    if node.right:
                        q1.append(node.right)
            for _ in range(size2):
                node = q2.popleft()
                if node:
                    level2.append(node.data)
                    if node.left:
                        q2.append(node.left)
                    if node.right:
                        q2.append(node.right)
            if Counter(level1) != Counter(level2):
                return False
        return not q1 and not q2
