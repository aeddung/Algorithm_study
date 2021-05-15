"""
N명의 학생 정보가 있따. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성해라.
1 <= N <= 100,000 / 학생 이름 길이와 성적은 모두 100 이하 자연수
"""
n = int(input())
data = []
for _ in range(n):
  input_data = input().split()
  data.append(input_data[0], int(input_data[1]))

data.sort(key=lambda x: x[1])
print(' '.join(x[0] for x in data))
