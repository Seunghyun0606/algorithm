# 배열의 크기 N은 10**5, k는 min(10**9, N**2) 보다 작거나 같은 수이다.
# A[i][j] = ixj 이고 이걸 일렬로 배열한 B[k] 값을 구해야한다.
# 배열 A, B 의 인덱스는 1부터 시작한다.
# 단순하게 배열을 만들면 메모리초과가 뜬다.

# 이분탐색을 이용해서, i*j의 값의 갯수를 세서, 인덱스 값을 구한다.
# 특정 값 이하의 수를 다 구하는 거니깐, 구간합도 가능할거 같은데?
# => 안된다, 왜냐면 결국 이분 탐색으로 구하는 mid값은 특정 값인 것이고,
# 그 특정 값일 때, 그 이하나 같은 숫자의 갯수를 구하는게 temp ( k ) 값이다.

# i*j 의 값은 min( 특정값(mid) //i, n )
# n*n 배열에서 n보다 갯수가 많을 수 는 없기 때문이다. ( ex 20//1 == 20이아니라 10 )

n = int(input())
k = int(input())

left = 1
# n**2여야하지 않나 싶지만, mid (특정값) 은 어찌됐든 인덱스 값보다 작을 수 밖에 없다.
right = k
answer = 0
while left <= right:
    mid = ( left + right ) // 2

    temp = 0
    for i in range(1, n+1):
        temp += min( mid//i, n )
    
    if temp >= k:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)