# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [(root, False)]
        while stack:
            curr, is_left = stack.pop()
            if not curr: # Null값인 경우 다시 while문 반복
                continue
            if not curr.left and not curr.right:
                if is_left: # left leaf인지 확인하는 용도
                    result += curr.val
            else:
                stack.append((curr.left, True))
                stack.append((curr.right, False)) # right leaf는 무조건 False
        return result
      
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(node, is_left):
            if not node:
                return 0
            
            if not node.left and not node.right and is_left:
                return node.val
            
            left_sum = traverse(node.left, True)
            right_sum = traverse(node.right, False)

            return left_sum + right_sum

        return traverse(root, False)   
