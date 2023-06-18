# setdefault 사용
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_n = len(candyType) // 2
        dic = {}
        for candy in candyType:
            dic.setdefault(candy, 0) # 두 번째 인자는 기본값
            dic[candy] += 1
        
        if max_n <= len(dic.keys()):
            return max_n
        else:
            return len(dic.keys())

# defaultdict 사용          
from collections import defaultdict
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_n = len(candyType) // 2
        dic = defaultdict(int) # 값을 지정하지 않은 키는 그 값이 0으로 지정됨
        for candy in candyType:
            dic[candy] += 1
        
        if max_n <= len(dic.keys()):
            return max_n
        else:
            return len(dic.keys())
