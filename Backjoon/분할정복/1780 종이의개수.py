# 쿼드트리인데, n이 2의 제곱승이 아닌 3의 제곱승
# -1, 0, 1로 구분한다.

# import sys
# input = sys.stdin.readline
# stdin이랑 큰 차이가 안나는거보니, 결국은 재귀에서 시간이 오래걸린다.
# 다른사람들 빨리한거 보니, for문으로 풀었더라

N = int(input())

papers = [ list(map(int, input().split())) for _ in range(N) ]

result = [0, 0, 0]

def NonaTree(i, j, n):

    check = papers[i][j]

    for row in range(i, i + n):
        for col in range(j, j + n):
            if papers[row][col] != check:
                NonaTree(i, j, n//3)
                NonaTree(i, j + n//3, n//3)
                NonaTree(i, j + n//3 + n//3, n//3)
                NonaTree(i + n//3, j, n//3)
                NonaTree(i + n//3 + n//3, j, n//3)
                NonaTree(i + n//3, j + n//3, n//3)
                NonaTree(i + n//3, j + n//3 + n//3, n//3)
                NonaTree(i + n//3 + n//3, j + n//3, n//3)
                NonaTree(i + n//3 + n//3, j + n//3 + n//3, n//3)
                
                return

    if check > 0:
        result[2] += 1
    elif check < 0:
        result[0] += 1
    else:
        result[1] += 1

NonaTree(0, 0, N)
print(*result, sep='\n')
