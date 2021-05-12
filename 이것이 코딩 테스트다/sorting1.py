"""
N명의 이름과 국어, 영어, 수학 점수가 주어진다. 아래 조건으로 학생 성적을 정렬하려고 한다.
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로(단, 아스키코드에서 대문자는 소문자보다 작으므로 사전 순으로 앞에 온다.)
1 <= N <= 100,000 / 점수는 1보다 크거나 갚고, 100보다 작거나 같은 자연수 / 이름은 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않는다.
"""
n = int(input())
students = []
for _ in range(n):
  students.append(list(input().split()))

# 국어, 영어, 수학, 이름 알파벳 순으로 비교
students = sorted(students, key=lambda student: (-int(student[1]), int(student[2]), -int(student[3]), student[0]))

for student in students:
  print(student[0])
