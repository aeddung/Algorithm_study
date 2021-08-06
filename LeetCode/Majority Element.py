# 직접 작성한 코드: 188ms
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter.keys():
                counter[num] += 1
                if counter[num] > len(nums) / 2:
                    return num
            else:
                counter[num] = 1
                if counter[num] > len(nums) / 2:
                    return num
                  
# 모범 참고 코드: 156ms
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_obj = Counter(nums)
        return max(count_obj.keys(), key=count_obj.get) # max(iterable object, key=기준이 되는 대상) <- count_obj.get(키 목록)
