# BJ.2628 종이자르기
# 가로(열) 세로(행) 준다
# 가로점선은 (행)을 자르는 것
# 세로점선은 (열)을 자르는 것

import sys

sys.stdin = open('input.txt', 'r')

col, row = map(int, input().split())

cut_n = int(input())

cut_info = [list(map(int, input().split())) for _ in range(cut_n)]
# 0이면 행을 자르고 1이면 열을 자른다.

cut_row = [cut_info[i][1] for i in range(len(cut_info)) if cut_info[i][0] == 0] + [0] + [row]
cut_row.sort()  # cut_row를 정돈함
cut_col = [cut_info[i][1] for i in range(len(cut_info)) if cut_info[i][0] == 1] + [0] + [col]
cut_col.sort()  # cut_col을 정돈함

my_row = []  # 각 가로 넓이들과 세로 넓이들 정보를 구해서 다 곱하면됨.
my_col = []  # 행, 또는 열을 안자를 경우 값이 나와야한다.

for r in range(1, len(cut_row)):  # 2, 3
    my_row.append(cut_row[r] - cut_row[r - 1])
for c in range(1, len(cut_col)):  # 4
    my_col.append(cut_col[c] - cut_col[c - 1])

max_square = 0

for r in my_row:
    for c in my_col:
        my_square = r * c
        if my_square > max_square:
            max_square = my_square

print(max_square)
