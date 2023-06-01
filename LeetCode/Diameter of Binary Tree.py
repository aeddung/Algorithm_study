# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# runtime: 57ms
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiameter = 0
        self.dfs(root)

        return self.maxdiameter

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left = self.dfs(root.left) # 왼쪽 노드의 높이(누적)
        right = self.dfs(root.right) # 오른쪽 노드의 높이(누적)

        self.maxdiameter = max(self.maxdiameter, left + right) # 최대 거리값 계산(현재 노드 높이와 무관)
        currheight = max(left, right) + 1 # 현재 노드 높이 계산
        return currheight
      
# runtime: 70ms      
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiameter = 0
        currheight = {}
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    leftheight = 0 if node.left == None else currheight.pop(node.left)
                    rightheight = 0 if node.right == None else currheight.pop(node.right)
                    maxdiameter = max(maxdiameter, leftheight + rightheight)
                    currheight[node] = max(leftheight, rightheight) + 1
                else:
                    stack.append((node, True))
                    stack.append((node.left, False))
                    stack.append((node.right, False))

        return maxdiameter
