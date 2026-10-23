''' BST Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def pairsViolatingBST(self, root):
        # code here
        arr = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            arr.append(node.data)
            inorder(node.right)

        inorder(root)

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums, 0

            mid = len(nums) // 2
            left, count_left = merge_sort(nums[:mid])
            right, count_right = merge_sort(nums[mid:])

            merged = []
            i = j = 0
            count = count_left + count_right

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    count += len(left) - i
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, count

        _, answer = merge_sort(arr)
        return answer

