# 투 포인터 활용
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0

        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1

        return res

# haspmap 활용      
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        dic = {}
        for i, v in enumerate(nums1):
            if v not in dic:
                dic[v] = 1
            else:
                dic[v] = dic[v] + 1

        for j, v in enumerate(nums2):
            if v in dic and dic[v] > 0:
                ans.append(v)
                dic[v] = dic[v] - 1

        return ans      
