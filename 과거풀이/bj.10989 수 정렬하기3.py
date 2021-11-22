# counting 정렬이용.

# import sys
# input = sys.stdin.readline

# total = int(input())

# # input_array 만들기
# input_array = []

# for _ in range(total):
#     input_array.append(int(input()))

# # count_array에서 10001 은 maximum 숫자
# count_array = [0]*10001
# output_array = [0]*total

# # 빈도수 counting하는 순간
# for i in input_array:
#     count_array[i] += 1

# # 빈도수의 누적합 만드는 과정
# for j in range(len(count_array)-1):
#     count_array[j+1] += count_array[j]

# # 정렬과정
# for k in range(total-1, -1, -1):
#     output_array[ count_array[input_array[k]] - 1 ] = input_array[k]
#     count_array[input_array[k]] -= 1

# print(*output_array, sep='\n') 

# import sys
# input = sys.stdin.readline

# total = int(input())

# result = [0]*10001

# for _ in range(total):
#     result[int(input())] += 1

# for i in range(10001):
#     if result[i]:
#         for j in range(result[i]):
#             print(i)

from collections import defaultdict
import sys

input = sys.stdin.readline

total = int(input())

count_dict = defaultdict(int)

for _ in range(total):
    count_dict[int(input())] += 1

for items in sorted(count_dict.items()):
    for i in range(items[1]):
        print(items[0])


