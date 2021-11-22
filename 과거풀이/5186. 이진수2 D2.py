# 5186.[파이썬 S/W 문제해결구현] 1일차 - 이진수2 D2

def Binary(num):
    global result, cnt
    while True:
        next_num = num * 2
        result += str(int(next_num))
        num = next_num - int(next_num)
        cnt += 1
        if num == 0.0:
            return

        if cnt > 13:
            return

TC = int(int(input()))
for tc in range(1, TC+1):
    num = float(input())
    result = ''
    cnt = 0
    Binary(num)

    if cnt > 13:
        print('#%d'%(tc), 'overflow')

    else:
        print('#%d %s'%(tc, result))