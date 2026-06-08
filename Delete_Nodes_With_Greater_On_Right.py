'''
Structure of linked list node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        # code here
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head = prev
        max_node = head
        curr = head
        while curr and curr.next:
            if curr.next.data < max_node.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_node = curr
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
