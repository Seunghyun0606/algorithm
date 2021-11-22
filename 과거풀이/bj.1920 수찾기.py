# 이분탐색


n = int(input())

A_list = sorted(list(map(int, input().split())))

m = int(input())

number_list = list(map(int, input().split()))

for number in number_list:
    start = 0
    end = n - 1
    while start <= end:
        mid = ( start + end ) // 2

        if A_list[mid] > number:
            end = mid - 1
        elif A_list[mid] < number:
            start = mid + 1
        else:
            print(1)
            break
    else:
        print(0)




# import sys
# input = sys.stdin.readline


# if __name__ == '__main__':
#     n = int(input())
#     map_1 = input().split()

#     m = int(input())
#     map_2 = input().split()

#     map_dict = {}
#     for i in map_1:
#         map_dict[i] = 0

#     for i in map_2:
#         if i in map_dict:
#             print(1)
#         else:
#             print(0)