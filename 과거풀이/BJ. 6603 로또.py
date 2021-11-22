# BJ. 6603 로또


def dfs(p, k, li):  # k 는 7, 로또번호 마지막 인덱스 1~7

    stack[p] = 1  # 첫 스택부터 쌓고 시작하자
    if len(li) == 6:
        print(*li)

    else:
        for j in range(p+1, k):
            if stack[j]:
                continue
            dfs(j, k, li + [a[j]])
            stack[j] = 0

import sys
sys.stdin = open('input.txt', 'r')

lotto_set = []
flag = True
while flag:  # 로또 set 만들기
    a = []
    for i in input().split():
        if i == '0':
            flag = False
            break
        a += [int(i)]
    if a:
        lotto_set += [a]  # 빈리스트 안넣어줄려고함.

for i in range(len(lotto_set)):
    a = lotto_set[i]  # 로또 첫 열, 7(로또 번호 수. 이중 6개뽑아야함)
    a1 = int(a[0])  # 7
    stack = [0] * (a1+1)  # 스택. 로또 셋의 첫열 안쓸거니깐.
    b = []

    dfs(0, a1+1, b)  # 7개 뽑는 dfs만들거야. 1은 스택 매개변수, b는 프린트할 리스트
    print()







