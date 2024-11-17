# 비트마스킹 연산으로해야함
import sys
input = sys.stdin.readline

n = int(input())
calc_list = [ tuple(input().split()) for _ in range(n) ]

S = set()

def add(S, p):
    S.add(p)
    return S

def remove(S, p):
    S.discard(p)
    return S

def check(S, p):
    # 겹치면 False 안겹치면 True
    print(0 if S.isdisjoint({p}) else 1)
    return S

def toggle(S, p):
    # 겹치면 False 안겹치면 True
    return remove(S, p) if S.isdisjoint({p}) else add(S, p)

def all(S, p):
    return { i for i in range(1, 20) }

def empty(S, p):
    S.clear()
    return S

for calc in calc_list:
    if len(calc) == 1:
        func, num = calc[0], 0
    else:
        func, num = calc
    process = f'{func}({S}, {num})'
    S = eval(process)


# import sys
# input = sys.stdin.readline

# my_set = 0

# check1 = []
# n = int(input())
# for _ in range(n):
#     my_input = input().split()
#     oper = my_input[0]

#     if oper == 'add':
#         my_set |= ( 1 << int(my_input[1]) )
#     elif oper == 'remove':
#         my_set &= ~( 1 << int(my_input[1]) )
#     elif oper == 'check':
#         if my_set & ( 1 << int(my_input[1]) ):
#             print(1)
#         else:
#             print(0)
#     elif oper == 'toggle':
#         my_set ^= ( 1 << int(my_input[1]) )
#     elif oper == 'all':
#         my_set = ( 1 << 21 ) - 1
#     elif oper == 'empty':
#         my_set = 0
