# runtime: 56ms
class Solution:
    def generateHelp(self, n: int, prev_level: List[int]) -> List[int]:
        if n <= 1: # 0층과 1층일 경우
            return [1] * (n + 1)
        
        new_level = [1] # 첫 번째 원소
        for i in range(1, n):
            new_level.append(prev_level[i - 1] + prev_level[i])
        new_level.append(1) # 마지막 원소 
        return new_level
    
    def generate(self, numRows: int) -> List[List[int]]:
        res_levels = [] # answer
        prev_res = [] # 이전 층
        
        for i in range(numRows):
            tmp_res = self.generateHelp(i, prev_res) # 새로운 층
            res_levels.append(tmp_res)
            prev_res = tmp_res
        
        return res_levels
      
# runtime: 36ms
class Solution:
  def generation(self, numRows: int) -> List[List[int]]:
    res = [[1] * i for i in range(1, numRows + 1)]
    for r in range(2, len(res)): # numRows 수
      for c in range(1, len(res[r]) - 1): # r번째 층(첫 번째와 마지막 원소는 1)
        res[r][c] = res[r - 1][c - 1] + res[r - 1][c]
    return res
