# 올림픽
# 금은동에 가중치를둬서 가장큰 나라가 1등하게 만들자

import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, input().split())

new_national = [ list(map(int, input().split())) for _ in range(n) ]
# 0은 나라 번호, 1 2 3 금은동 순서

national = []  # 국가가 1, 2, 3, 4 순서가아니라 1, 4, 3, 2라고 들어올수있기 때문에 정렬해준다.

j = 0
while len(national) < n:
    j += 1
    for i in range(n):
        if new_national[i][0] == j:
            national.append(new_national[i])
            break
rank = []

for i in range(n):  # 국가뽑아
    rank.append(national[i][1]*(10**1000) + national[i][2]*(10**50) + national[i][3])

asc_rank = sorted(rank)
flag = False
for i in range(len(rank)):
    if flag:
        break
    for j in range(len(asc_rank)-1, -1, -1):  # 가장큰값부터 꺼내야한다.
        if asc_rank[j] == rank[i] and i == k-1:
            print(n-j)
            flag = True
            break

