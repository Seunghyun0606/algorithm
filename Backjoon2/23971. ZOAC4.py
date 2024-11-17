# 3 - 1 5 9 13  bc + 1 = a > c = ( a-1) // (b+1) +1
# 2 - 1 4 7 10 3n+1
# 1 - 1 3 5 7 2n+1 

import sys
input = sys.stdin.readline

# print(input)

tab_col, tab_row, emp_col, emp_row = list(map(int, input().split()))
col = (tab_col-1) // (emp_col+1) +1
row = (tab_row-1) // (emp_row+1) +1
max_person = col * row

# print(col, row)
print(max_person)


