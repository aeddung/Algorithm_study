# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ans = []
        while q:
            sum_ = 0
            count = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    sum_ += node.val
                    count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(sum_ / count)
        
        return ans

# DFS
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lvlcnt = defaultdict(int)
        lvlsum = defaultdict(int)

        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return
            lvlcnt[level] += 1
            lvlsum[level] += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return [lvlsum[i] / lvlcnt[i] for i in range(len(lvlcnt))]  
