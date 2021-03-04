# 비트 연산 활용, 20개의 0을 집합의 원소로 사용한다.
# add = or 연산 (추가)
# remove = and + not연산, 
# check = and 연산
# toggle = xor연산 + 1
# all = S 전체를 on으로 바꿈 1~20
# empty = S 전체를 공집합으로 바꿈 off

# try except 쓰면 4028ms
# 안쓰면 3532ms 확실히 try except가 먹는 시간이 있네.
import sys
input = sys.stdin.readline

my_set = 0

n = int(input())
for _ in range(n):
    my_input = input().split()
    # try:
    #     if my_input[1]:
    #         k = int(my_input[1])
    # except:
    #     pass
    oper = my_input[0]

    if oper == 'add':
        my_set |= ( 1 << int(my_input[1]) )
    elif oper == 'remove':
        my_set &= ~( 1 << int(my_input[1]) )
    elif oper == 'check':
        if my_set & ( 1 << int(my_input[1]) ):
            print(1)
        else:
            print(0)
    elif oper == 'toggle':
        my_set ^= ( 1 << int(my_input[1]) )
    elif oper == 'all':
        my_set = ( 1 << 21 ) - 1
    elif oper == 'empty':
        my_set = 0

# 리스트로 비트마스킹 구현. 3476ms
# import sys
# input = sys.stdin.readline
# M = int(input())
# eset = [0]*21

# for _ in range(M):
#     oper = input().split()
#     if oper[0] == 'add':
#         eset[int(oper[1])] = 1
#     elif oper[0] == 'remove':
#         eset[int(oper[1])] = 0
#     elif oper[0] == 'check':
#         print(1 if eset[int(oper[1])] else 0)
#     elif oper[0] == 'toggle':
#         eset[int(oper[1])] = 0 if eset[int(oper[1])] else 1
#     elif oper[0] == 'all':
#         eset = [1]*21
#     else:
#         eset = [0]*21