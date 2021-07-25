class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter.keys():
                counter[num] = 2
            else:
                counter[num] = 1
        
        for key, value in counter.items():
            if value == 1:
                return key
              
# 참고 모범 코드
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer = answer ^ num
        return answer
