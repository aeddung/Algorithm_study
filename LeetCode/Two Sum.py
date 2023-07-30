class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        # 미리 해시테이블 값 채워넣기
        for i in range(len(nums)):
            numMap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        
        return

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return  
