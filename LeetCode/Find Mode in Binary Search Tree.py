# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# runtime: 68ms
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(node, l):
            if node is None:
                return l
            
            if node.val in l:
                l[node.val] += 1
            else:
                l[node.val] = 1

            if node.left is not None:
                bfs(node.left, l)
            if node.right is not None:
                bfs(node.right, l)
            
            return l

        l = dict()
        bfs(root, l)
        m = max(l.values())

        return [i for i, v in l.items() if v == m]
      
# runtime: 62ms
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(freq):
            queue = [root]
            while queue:
                curr = queue.pop() # queue는 항상 길이가 1인 리스트 -> 그 1개의 원소는 트리노드, 즉 recursive 구조가 아니라 트리노드(자식노드)를 queue에 넣어가면서 freq 업데이트
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                   
                # if문을 사용할 필요가 없는 dictionary 값 설정 방법
                freq.setdefault(curr.val, 0) # setdefault(key, default): key가 있으면 value 반환, 없다면 default 값을 value로 설정
                freq[curr.val] += 1
        
        freq = {}
        bfs(freq)
        ans = []
        max_cnt = 0

        # 최댓값 찾기
        for i, v in freq.items():
            if v > max_cnt:
                max_cnt = v
        
        for i, v in freq.items():
            if v == max_cnt:
                ans.append(i)
        
        return ans
