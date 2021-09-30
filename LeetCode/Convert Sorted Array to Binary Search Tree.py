# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # runtime: 60ms
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # base case
        if not nums:
            return
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid]) # 기준이 되는 root 노드는 매번 생성
        # 재귀반복
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root
