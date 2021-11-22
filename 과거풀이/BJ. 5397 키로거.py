# BJ. 5397 키로거
# insert 하나해보고 10^6개 리스트 만들어서 하나해보자.
# 일단 문제의도는 연결리스트 만들라는거 같긴하다.

import sys

T = int(input())

for tc in range(T):

    idx = 0
    result = []

    for password in list(sys.stdin.readline()):
        if password == '<':
            if idx > 0:
                idx -= 1
        elif password == '>':
            if len(result) > idx:
                idx += 1
        elif password == '-':
            if result and idx > 0:
                result.pop(idx-1)
                idx -= 1
        else:
            result.insert(idx, password)
            idx += 1

    print(*result, sep='')


