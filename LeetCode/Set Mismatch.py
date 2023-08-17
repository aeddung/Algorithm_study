# 수학적 계산법
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = n * (n + 1) // 2 # 실제 정상 원소들의 합
        miss = s - sum(set(nums))
        duplicate = sum(nums) + miss - s
        return [duplicate, miss]

from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        op = [0, 0]
        for i in range(1, len(nums) + 1):
            if counts[i] == 2:
                op[0] = i
            if counts[i] == 0:
                op[1] = i
        
        return op  

# Counter 메서드를 사용하지 않은 나이브 코드
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = {}
        ans = [0, 0]
        for i in range(1, len(nums) + 1):
            dic[i] = 0
        
        for n in nums:
            dic[n] += 1
        
        for k, v in dic.items():
            if v == 2:
                ans[0] = k
            if v == 0:
                ans[1] = k
            
        return ans
