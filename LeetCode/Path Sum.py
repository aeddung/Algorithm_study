# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# runtime: 44ms
class Solution:
    def dfs(self, node: Optional[TreeNode], total: int):
        if not node:
            return 
        
        total -= node.val
        if not node.left and not node.right and total == 0:
            self.ans = True
        
        self.dfs(node.left, total)
        self.dfs(node.right, total)
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = False
        
        self.dfs(root, targetSum)
        return self.ans
     
# runtime: 40ms    
class Solution:
	def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.right and not root.left:
            if targetSum == root.val:
                return True
            else:
                return False
        else:
            total = root.val
            return self.hasPathSum(root.left, targetSum - total) or self.hasPathSum(root.right, targetSum - total)
