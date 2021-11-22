from itertools import combinations
# import sys
# input = sys.stdin.readline

while True:
    mine = list(map(int, input().split()))
    if mine[0]:
        for comb in combinations(mine[1:], 6):
            print(*comb)
        print()
    else:
        break

