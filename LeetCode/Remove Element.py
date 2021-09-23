# 투-포인터 알고리즘 사용
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
      

# 파이썬 내장 함수 count 사용 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val):
            nums.remove(val)
        return len(nums)
