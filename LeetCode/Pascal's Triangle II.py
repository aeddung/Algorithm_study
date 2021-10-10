# runtime: 32ms
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        
        res = [[1] * i for i in range(1, rowIndex + 2)] # 문제에서 0-indexed라고 했기 때문에 +2를 해줘야 함
        for r in range(2, len(res)):
            for c in range(1, len(res[r]) - 1):
                res[r][c] = res[r - 1][c - 1] + res[r - 1][c]
        
        return res[rowIndex]
