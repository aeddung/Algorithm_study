# runtime: 2568ms
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        while i < len(numbers):
            if target - numbers[i] in numbers:
                return [i + 1, numbers[i + 1:].index(target - numbers[i]) + i + 2]
            else:
                i += 1
                
# runtime: 60ms                
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            curr = numbers[i]
            rem = target - curr

            if rem in dic and dic[rem] != i:
                min_ = min(i + 1, dic[rem] + 1)
                max_ = max(i + 1, dic[rem] + 1)
                return [min_, max_]
            else:
                dic[curr] = i                
