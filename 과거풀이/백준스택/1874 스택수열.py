# 스택문제, n개 받아서 수열을 이룰수 있는지 알아보자
import sys
input = sys.stdin.readline
n = int(input())
possi = [ int(input()) for _ in range(n)]

stack = []
result = []
k = 0
for i in range(1, n+1):

    stack.append(i)
    result.append('+')
    while stack and k < n and possi[k] == stack[-1]:
        stack.pop()
        result.append('-')
        k += 1
if not stack:
    print(*result, sep='\n')
else:
    print('NO')
    