# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ''
        
        output = str(root.val)

        if (root.left != None or root.right != None):
            output += '(' + self.tree2str(root.left) + ')'
        
        if root.right != None:
            output += '(' + self.tree2str(root.right) + ')'
        
        return output

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ''
        
        output = str(root.val)

        if root.left:
            output += '({})'.format(self.tree2str(root.left))
        if root.left is None and root.right: # 오른쪽 노드는 있는데 왼쪽 노드는 없는 경우 one-to-one 매핑을 위해 '()' 문자열 추가
            output += '()'

        if root.right:
            output += '({})'.format(self.tree2str(root.right))

        return output  
