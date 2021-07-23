# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BST(iteration)
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        level = 0
        if not root:
            return 0
        q = deque([root])
        
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            
        return level
 
# Recursive
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_level = self.maxDepth(root.left) + 1
        right_level = self.maxDepth(root.right) + 1
        
        return max(left_level, right_level)
