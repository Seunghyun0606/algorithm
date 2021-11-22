# 표준입출력관련

# 4402ms 나옴
# n = int(input())

# stack = []
# for _ in range(n):
#     temp = int(input())
#     if not temp and stack:
#         stack.pop()
#     else:
#         stack.append(temp)
# print(sum(stack))

# 이런식으로하면 표준입출력이 좀 다른가본데? code에서는 안돌아간다.
# 근데 훨씬빠르다. 96ms
# from sys import stdin

# n = int(input())

# stack = []
# for temp in map(int, stdin):
#     if not temp and stack:
#         stack.pop()
#     else:
#         stack.append(temp)
# print(sum(stack))

# readline은 112ms
import sys

n = int(input())

stack = []
for _ in range(n):
    temp = int(sys.stdin.readline())
    if not temp and stack:
        stack.pop()
    else:
        stack.append(temp)
print(sum(stack))
