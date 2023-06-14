# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# runtime: 69ms
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0

        def helper(node: TreeNode) -> int:
            if not node:
                return 0
            
            left_sum = helper(node.left)
            right_sum = helper(node.right)
            tilt = abs(left_sum - right_sum) # 방문한 노드의 '왼쪽 leaf 노드 및 오른쪽 leaf 노드 차이'의 절댓값 업데이트

            self.total_tilt += tilt

            return left_sum + right_sum + node.val # 부모 노드의 tilt를 구하기 위해 현재 node.val 더해주기

        helper(root)
        return self.total_tilt
      
# memory: 17.9MB(77% Beats)      
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        child_dict = {}
        stack = [(root, False)]
        total_tilt = 0

        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
            else:
                left_sum = 0 if node.left is None else child_dict.pop(node.left)
                right_sum = 0 if node.right is None else child_dict.pop(node.right)
                tilt = abs(left_sum - right_sum)
                total_tilt += tilt
                child_dict[node] = left_sum + right_sum + node.val
            
        return total_tilt      
