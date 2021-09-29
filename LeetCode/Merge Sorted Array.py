# runtime: 36ms
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer = len(nums1) - 1
        m -= 1 # 리스트 원소를 뒤에서부터 접근
        n -= 1
        
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[pointer] = nums1[m]
                m -= 1
            else:
                nums1[pointer] = nums2[n]
                n -= 1
            pointer -= 1
            
        if n >= 0: # m은 남든 말든 상관없음(m이 남으면 nums2 원소가 크다는 것이고, 남지 않았다면 nums1 원소가 크다는 것인데 이미 뒤에서부터 채웠기 때문)
            nums1[:n + 1] = nums2[:n + 1]
            
# runtime: 40ms
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m + n):
            # 해당 원소가 0이고 이후 길이가 nums2 길이와 같으면 기존 nums1 원소는 남은 nums2 원소보다 작은 상태
            if nums1[i] == 0 and len(nums1[i:]) == len(nums2):
                nums1[i:] = nums2
                break
            if len(nums2) > 0 and nums2[0] < nums1[i]:
                nums1[i:] = nums2[:1] + nums1[i:-1] # 새로운 nums2 원소 추가, 나머지 원소 오른쪽으로 shift
                nums2 = nums2[1:] # nums2 업데이트, 즉 맨 왼쪽 원소 
