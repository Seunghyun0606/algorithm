# 1일 경우
# 1234 => (n-1)!
# 24 3
# 1234 1
# 5678 2 1 3 4 -> 5번째
# (k // n)+1 부터 만들어서 k % n 번째 찾으면된다
# 즉 이걸 여러번 반복하면 횟수를 엄청 줄일수있다.
# 2일 경우 반대. 하지만 구하기 너무귀찮다.

n = int(input())
quiz = list(map(int, input().split()))

check = [0]*(n+1)

k*n 
def comb()



# 실패, 20까지 n이 들어올 수 있기때문에, 모두 만들면 메모리초과가 난다.
# from itertools import permutations as p

# n = int(input())
# check = list(map(int, input().split()))

# my_permu = list(p([ i+1 for i in range(n)], n))

# if check[0] == 1:
#     # k번째 순열
#     print(my_permu[check[1]-1])
# else:
#     # 순열이 몇번째꺼인지
#     print(my_permu.index(tuple(check[1:]))+1)
