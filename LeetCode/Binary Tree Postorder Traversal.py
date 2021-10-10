# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, result):
        if not root:
            return
        
        self.dfs(root.left, result)
        self.dfs(root.right, result)
        result.append(root.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, result)
        return result
