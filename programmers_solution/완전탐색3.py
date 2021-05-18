"""
"""
# 직접 작성한 코드 버전 1
import math
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    result = []
    for i in range(1, int(math.sqrt(total)) + 1):
        if total % i == 0:
            result.append([total // i, i])
    for size in result:
        if (size[0] - 2) * (size[1] - 2) >= yellow:
            return size
          
# 직접 작성한 코드 버전 2
import math
def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, int(math.sqrt(total)) + 1):
        if total % i == 0:
            if (total // i - 2) * (i - 2) >= yellow:
                return [total // i, i]
