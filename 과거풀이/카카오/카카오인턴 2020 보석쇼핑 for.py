# 더블포인터를쓴다.
# L, R을 0번 인덱스에서 시작해서 R을 오른쪽으로 계속 늘려가다가, 조건을 만족하게 되면
# L을 오른쪽으로 늘리고, 조건을 만족하지않는순간 다시 R을 오른쪽으로 늘린다.
# 이때의 구간의 최소 길이를 구한다.
from collections import defaultdict

def solution(gems):
    answer = []

    gem_kind = len(set(gems))  # 중복제거
    all_gems = len(gems)  # 전체 gems수
    check = defaultdict(int) # key가 없으면 기본값 int, 있으면 값 있는거 출력, setdefault 보다 빠르다. d = {} d.setdefault(k, 0)
    left = 0
    right = 0

    candidate = []
    flag = True
    while flag:
        kind = len(check)
        if right == all_gems:
            break

        for i in range(left, right):
            # for문으로 돌리는 효과적인 방법 모르겠군.

            


    min_length = 100000
    
    for s, e in candidate:
        temp = e - s
        if min_length > temp:
            min_length = temp
            answer = [s+1, e]


    return answer
