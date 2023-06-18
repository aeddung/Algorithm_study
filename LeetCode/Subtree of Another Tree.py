# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot: # 서브트리가 없는 경우 역시 True
            return True

        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if not root and not subRoot: # leaf 노드일 때를 가리킴 <- 여기까지 온 경우라면 재귀 구조에서 상위로 가면서 모두 True를 리턴하게 됨
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))

        return False
