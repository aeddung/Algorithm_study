class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        
        for i in range(len(grid)): # 행 살펴보기
            for j in range(len(grid[i])): # 열 살펴보기
                if grid[i][j] == 1: # land 여부 확인
                    # land인 셀 주변(위, 왼쪽, 아래, 오른쪽) 확인
                    if i == 0 or grid[i-1][j] == 0: # above(i 파악은 맨 위쪽에 위치한지 파악)
                        perimeter += 1
                    if j == 0 or grid[i][j-1] == 0: # left(j 파악은 맨 왼쪽에 위치한지 파악)
                        perimeter += 1
                    if i == len(grid)-1 or grid[i+1][j] == 0: # below(i 확인은 맨 아래쪽에 위치한지 파악)
                        perimeter += 1
                    if j == len(grid[i])-1 or grid[i][j+1] == 0: # right(j 확인은 맨 오른쪽에 위치한지 파악)
                        perimeter += 1
        
        return perimeter
