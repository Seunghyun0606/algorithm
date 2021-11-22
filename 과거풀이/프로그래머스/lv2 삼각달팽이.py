# 방향은 3개다, 밑, 오른쪽, 좌측위
# 정삼각형이아니라, 직각삼각형이라 생각하고 풀어야한다.
def solution(n):
    answer = []
    check = [ [0]*n for _ in range(n) ]

    r, c = -1, 0  # 초기 시작을 +1주고 하기위함
    num = 0

    for i in range(n):
        for j in range(i, n):
            # down
            if i % 3 == 0:
                r += 1
            # right
            elif i % 3 == 1:
                c += 1
            # left up
            else:
                r -= 1
                c -= 1
            
            num += 1
            check[r][c] = num
    for che in check:
        for c in che:
            if c:
                answer.append(c)
    return answer