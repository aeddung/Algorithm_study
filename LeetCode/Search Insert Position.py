# 직접 작성한 코드
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
          
# 모범 참고 코드
class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    # binary search
    left, right = 0, len(nums) - 1
    while right >= left:
      mid = (left + (right - left)) // 2 # 파이썬은 상관없으나 다른 언어에선 숫자가 커지면 truncated될 수 있음
      if target > nums[mid]:
        left = mid + 1
      elif target < nums[mid]:
        right = mid - 1
      else:
        return mid
    return left # nums 원소가 모두 유니크한 값이므로 오른쪽 원소가 항상 큼 -> 따라서 새롭게 추가되는 원소는 left 위치에 와야 
