# 분할정복개념.
# QuardTree를 만들어야한다.

N = int(input())
papers = [ list(map(int, input().split())) for _ in range(N) ]

blue, white = 0, 0

def QuardTree(i, j, n):
    global blue, white

    color = papers[i][j]

    for row in range(i, i + n):
        for col in range(j, j + n):
            if papers[row][col] != color:
                QuardTree(i, j, n//2)
                QuardTree(i, j + n//2, n//2)
                QuardTree(i + n//2, j, n//2)
                QuardTree(i + n//2, j + n//2, n//2)

                return
    if color:
        blue += 1
    else:
        white += 1


QuardTree(0, 0, N)
print(white, blue, sep='\n')