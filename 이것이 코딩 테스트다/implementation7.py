"""
문제 설명: https://programmers.co.kr/learn/courses/30/lessons/60059
"""
# 시계방향 90도 회전
def rotate_matrix_90_degree(x):
    n = len(x) # 행 길이
    m = len(x[0]) # 열 길이
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = x[i][j]
    return result

# 자물쇠 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3 # 중앙 부분에 있는 자물쇠
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 크기를 기존 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠 중앙에 기존 자물쇠 끼워넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    # 4가지 방향 확인 -> 회전 4번 다 해본다고 생각
    for rotation in range(4):
        key = rotate_matrix_90_degree(key)
        for x in range(n * 2): # 2배를 하는 이유는 열쇠와 자물쇠가 전혀 겹치지 않을 때 최대 길이가 n * 2이기 때문
            for y in range(n * 2):
                # 자물쇠에 열쇠 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j] # 겹치지 않는 부분은 아무런 변화가 없음
                        
                # 자물쇠에 열쇠가 들어맞는지 확인
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
