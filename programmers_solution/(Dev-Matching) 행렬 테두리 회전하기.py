"""
https://programmers.co.kr/learn/courses/30/lessons/77485
"""

# 참고 코드
def solution(rows, columns, queries):
    answer = []
    # 행렬 만들기
    array = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1
    
    for x1, y1, x2, y2 in queries:
        tmp = array[x1 - 1][y1 - 1] # 가로로 옮겨질 값 저장
        mini = tmp
        
        # 왼쪽 세로
        for k in range(x1 - 1, x2 - 1):
            test = array[k + 1][y1 - 1]
            array[k][y1 - 1] = test
            mini = min(mini, test)
            
        # 하단 가로
        for k in range(y1 - 1, y2 - 1):
            test = array[x2 - 1][k + 1]
            array[x2 - 1][k] = test
            mini = min(mini, test)
            
        # 오른쪽 세로
        for k in range(x2 - 1, x1 - 1, -1):
            test = array[k - 1][y2 - 1]
            array[k][y2 - 1] = test
            mini = min(mini, test)
            
        # 상단 가로
        for k in range(y2 - 1, y1 - 1, -1):
            test = array[x1 - 1][k - 1]
            array[x1 - 1][k] = test
            mini = min(mini, test)
        
        array[x1 - 1][y1] = tmp
        answer.append(mini)
    return answer
