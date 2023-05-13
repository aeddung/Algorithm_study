class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')

        head = len(s) % k
        grouping = []

        if head: # 문자 갯수가 홀수개일 경우 맨 앞 그룹에 넣기
            grouping.append(s[:head])
        for i in range(head, len(s), k):
            grouping.append(s[i:i + k])

        return '-'.join(grouping).upper()
