class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
   
        for idx, (key, value) in enumerate(dic.items()):
            if value == 1:
                return s.index(key)
        
        return -1
        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        queue = []
        for i, v in enumerate(s):
            if c not in dic:
                dic[v] = i
                queue.append(v)
            else:
                if v in queue:
                    queue.remove(v)
        if queue:
            return dic[queue[0]]
        else:
            return -1
