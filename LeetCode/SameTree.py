# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# binary serach tree(runtime: 32ms)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        
        return (p.val == q.val) and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
      
# stack iteration(runtime: 32ms)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop()
            if p and q and p.val == q.val:
                # stack = [(p.left, q.left), (p.right, q,right)]
                stack.extend([
                    (p.left, q.left),
                    (p.right, q.right)
                ])
            elif p or q:
                return False
        return True
