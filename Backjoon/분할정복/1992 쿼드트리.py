# 색종이 만들기와 유사하다. 다만 어디에서 괄호를 씌우고 닫을지 생각해봐야할듯.
# 기본적으로 분할이 시작할때, 괄호가 들어가야한다.
# 3, 2, 4, 1 사분면 순서 (좌상, 우상, 좌하, 우하)

N = int(input())
data = [ list(map(int, input())) for _ in range(N) ]

result = []
def QuardTree(i, j, n):

    check = data[i][j]

    for row in range(i, i + n):
        for col in range(j, j + n):
            if data[row][col] != check:
                result.append('(')
                QuardTree(i, j, n//2)  # 3사분면
                QuardTree(i, j + n//2, n//2)  # 2사분면
                QuardTree(i + n//2, j, n//2)  # 4사분면
                QuardTree(i + n//2, j + n//2, n//2)  # 1사분면
                result.append(')')
                return
    if check:
        result.append('1')
    else:
        result.append('0')

QuardTree(0, 0, N)

print(''.join(result))