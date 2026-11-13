''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        # code here
        def inorder(root, result):
            if root is None:
                return

            inorder(root.left, result)
            result.append(root.data)
            inorder(root.right, result)

        list1 = []
        list2 = []

        inorder(r1, list1)
        inorder(r2, list2)

        i = 0
        j = 0
        result = []

        while i < len(list1) and j < len(list2):
            if list1[i] == list2[j]:
                result.append(list1[i])
                i += 1
                j += 1

            elif list1[i] < list2[j]:
                i += 1

            else:
                j += 1

        return result
