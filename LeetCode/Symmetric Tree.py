# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        left_visited = []
        right_visited = []
        
        q = deque()
        
        # left subtree
        if root.left:
            q.append((root.left, root.left.val))
        while q:
            n, v = q.popleft()
            left_visited.append(v)
            
            if v == None:
                continue
            
            if n.left:
                q.append((n.left, n.left.val))
            else:
                q.append((n.left, None))
            
            if n.right:
                q.append((n.right, n.right.val))
            else:
                q.append((n.right, None))
        
        if root.right:
            q.append((root.right, root.right.val))
        while q:
            n, v = q.popleft()
            right_visited.append(v)
            
            if v == None:
                continue
            
            if n.right:
                q.append((n.right, n.right.val))
            else:
                q.append((n.right, None))
            
            if n.left:
                q.append((n.left, n.left.val))
            else:
                q.append((n.left, None))
                
        if left_visited == right_visited:
            return True
        else:
            return False
