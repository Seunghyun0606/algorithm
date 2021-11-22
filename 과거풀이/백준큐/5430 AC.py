# 단순히 뒤집기만하면 reverse가 O(n) 이라 진행이안된다. 뒤집으면 뒤에서 빼던가 하면됨.

from collections import deque
# import sys
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    where = True
    func = input()
    n = int(input())
    temp = input().strip('[]')
    if temp:
        array = deque(temp.split(','))
        # [2,1] 이랑 [2, 1] 은 다르다던데 별로 상관없는데? 원래라면 아래코드처럼해야할듯하다.
        # array = deque(map(lambda x: x.strip(' '), temp.split(',')))
        try:
            for p in func:
                if p == 'R':
                    where = not where
                else:
                    array.popleft() if where else array.pop()
            print('[' + ','.join(list(array)) + ']') if where else print('[' + ','.join(list(reversed(array))) + ']')
        except:
            print('error')
    else:
        # R는 오류가 아니다 D만 오류이다. 이거때매 많이 틀렸네 ㅡㅡ
        print('error') if 'D' in func else print('[]')
