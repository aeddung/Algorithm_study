# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        self.dfs(root, visited)
        return visited
    
    def dfs(self, root: TreeNode, visited):
        if root == None:
            return
        
        visited.append(root.val)
        self.dfs(root.left, visited)
        self.dfs(root.right, visited)
