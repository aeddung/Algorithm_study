"""
문제 설명
n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 2 이상 100 이하인 자연수입니다.
wires는 길이가 n-1인 정수형 2차원 배열입니다.
wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
1 ≤ v1 < v2 ≤ n 입니다.
전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

입출력 예
n	wires	result
9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
4	[[1,2],[2,3],[3,4]]	0
7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	1
"""

# 참고한 코드(BFS)
from collections import deque
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs(start):
        visited = [0] * (n + 1)
        q = deque([start])
        visited[start] = 1
        cnt = 1 # 현재 전력망에 포함된 노드 갯수
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        return cnt
    
    print(graph)
    
    res = n
    for a, b in wires:
        # a와 b노드 사이를 끊었을 경우 고려 -> 2개의 전력망으로 구분하여 노드 갯수 차이 구하기
        graph[a].remove(b)
        graph[b].remove(a)
        
        res = min(abs(bfs(a) - bfs(b)), res)
        
        # 끊었던 노드들 복구
        graph[a].append(b)
        graph[b].append(a)
    
    return res

# UF(union find) 알고리즘 
def find(x, parent):
    if parent[x] < 0:
        return x # 부모 테이블상에서 부모를 자기 자신으로 초기화하
    parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    root_a = find(a, parent)
    root_b = find(b, parent)
    
    if root_a < root_b:
        parent[root_a] += parent[root_b] # 루트노드의 parent값 절댓값은 트리 크기 의미
        parent[root_b] = root_a  
    else: # root_a > root_b
        parent[root_b] += parent[root_a]
        parent[root_a] = root_b

def solution(n, wires):
    answer = n
    for exclude in range(n - 1):
        parent = [-1] * (n + 1)
        
        # 간선을 차례대로 제외하면서 나머지 간선들로 유니온 파인드 진행
        for a, b in (wires[:exclude] + wires[exclude + 1:]):
            union(a, b, parent)
            
        # 제외한 간선의 양 끝 점은 서로 독립된 트리의 어느 한 점으로,
        # 그 두 점의 루트 노드의 parent 값의 차의 절댓값이 두 트리 사이의 노드 개수 차이
        sub_cnt1 = parent[find(wires[exclude][0], parent)]
        sub_cnt2 = parent[find(wires[exclude][1], parent)]
        answer = min(answer, abs(sub_cnt2 - sub_cnt1))
    return answer
