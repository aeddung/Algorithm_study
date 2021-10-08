# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if root.left and root.right: # 왼쪽, 오른쪽 자식이 모두 있는 경우
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else: # 한쪽으로 쏠린 skewed tree의 경우 최대 깊이를 구해줘야 함
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
