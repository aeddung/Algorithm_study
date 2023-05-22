# 78ms
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = []
        mapping = {}
        
        for i, s in enumerate(sorted(score, reverse=True)):
            mapping[s] = i + 1

        for s in score:
            rank = str(mapping[s])
            if rank == '1':
                rank = 'Gold Medal'
            elif rank == '2':
                rank = 'Silver Medal'
            elif rank == '3':
                rank = 'Bronze Medal'
            
            answer.append(rank)
        
        return answer

# runtime: 97ms      
from heapq import heappush, heappop

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [''] * len(score)
        rankings = []

        for i, v in enumerate(score):
            heappush(rankings, (-v, i)) # 가장 작은 숫자가 맨 왼쪽에 위치
        
        r = 1
        rank = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        while len(rankings) != 0:
            _, i = heappop(rankings) # 가장 작은 숫자부터 제거
            if r <= 3:
                ans[i] = rank[r - 1]
            else:
                ans[i] = f'{r}'
            r += 1
        
        return ans      
