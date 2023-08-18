class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            # mid 자리에 대응되는 행렬 자리(row, column) 찾기
            mid_row, mid_col = divmod(mid, n) # divmode(a, b): a를 b로 나눈 몫과 나머지 동시에 리턴

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
