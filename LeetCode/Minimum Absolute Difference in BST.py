# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# runtime: 72ms
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res, pre = inf, inf
        def dfs(n: Optional[TreeNode]) -> None:
            if not n:
                return
            
            dfs(n.left)
            nonlocal res # nonlocal: 중첩 함수 내에서 상위 함수의 변수를 참조
            nonlocal pre
            res, pre = min(res, abs(pre - n.val)), n.val
            dfs(n.right)

        dfs(root)
        return res

# runtime: 47ms      
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        d = float('inf')
        s = [] # 연속되는 노드 추가
        if root == None:
            return
          
        d = self.dfs(root, d, s)
        return d

    def dfs(self, root: Optional[TreeNode], d: float, s: List[int]) -> int:
        if root.left != None:
            d = self.dfs(root.left, d, s)
        s.append(root.val)

        if len(s) > 1:
            diff = abs(s[-1] - s[-2])
            if diff < d:
                d = diff
        
        if root.right != None:
            d = self.dfs(root.right, d, s)
        return d      
