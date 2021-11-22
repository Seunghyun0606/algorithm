# 4613. 러시아 국기 같은 깃발
# 첫줄은 기본적으로 하얀색으로 바꾼다
# 둘째줄에서 파란색과 하얀색이 같으면 파란색으로 바꾼다.
# 셋째줄에서 파란색과 빨간색이 같으면 빨간색으로 바꾼다.

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())

    flag = [ [ 0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for color in input():




