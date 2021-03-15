# 배열의 크기 N은 10**5, k는 min(10**9, N**2) 보다 작거나 같은 수이다.
# A[i][j] = ixj 이고 이걸 일렬로 배열한 B[k] 값을 구해야한다.
# 배열 A, B 의 인덱스는 1부터 시작한다.

n = int(input())
k = int(input())

A = [ [ i*j for j in range(1, n+1) ] for i in range(1, n+1) ]
B = []

for i in range(1, n+1):
    for j in range(1, n+1):
        B.append