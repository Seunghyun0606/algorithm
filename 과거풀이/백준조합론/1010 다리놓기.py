from math import factorial as f
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    print(int(f(m)/(f(m-n)*f(n))))

