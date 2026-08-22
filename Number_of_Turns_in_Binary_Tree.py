''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def numberOfTurns(self, root, p, q):
        # code here
        def find_path(node,target, path):
            if not node:
                return False
            if node.data == target:
                return True
            path.append('L')
            if find_path(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if find_path(node.right, target, path):
                return True
            path.pop()
            return False
        def find_lca(node, p, q):
            if not node:
                return None
            if node.data == p or node.data == q:
                return node
            left = find_lca(node.left, p, q)
            right = find_lca(node.right, p, q)
            if left and right:
                return node
            return left if left else right
        lca = find_lca(root, p, q)
        if not lca:
            return -1
        path_p = []
        path_q = []
        find_path(lca, p, path_p)
        find_path(lca, q, path_q)
        # If one node is the LCA
        if not path_p or not path_q:
            path = path_p if path_p else path_q
            turns = 0
            for i in range(1, len(path)):
                if path[i] != path[i - 1]:
                    turns += 1
            return turns if turns > 0 else -1
        # Reverse path from p to LCA
        path_p.reverse()
        # Complete path: p -> LCA -> q
        path = path_p + path_q
        turns = 0
        for i in range(1, len(path)):
            if path[i] != path[i - 1]:
                turns += 1
        return turns if turns > 0 else -1
