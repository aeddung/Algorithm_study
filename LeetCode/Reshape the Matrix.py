class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat
        flatten = [] # 기존 matrix 한 줄로 늘여놓기
        for i in mat:
            for j in i:
                flatten.append(j)

        ans = []
        for i in range(0, len(flatten), c): # 컬럼(c) 기준으로 reshape
            ans.append(flatten[i:i+c])
        return ans
