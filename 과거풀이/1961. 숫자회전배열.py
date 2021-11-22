# 1961. 숫자회전배열

def my_rotate(arr):  # 90도 회전
    new_arr = [ [ 0 for _ in range(len(arr)) ] for _ in range(len(arr)) ]
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            new_arr[y][len(arr)-1-x] = arr[x][y]
    return new_arr

T = int(input())

for tc in range(T):
    n = int(input())

    my_arr = [ list(map(int, input().split())) for _ in range(n)]

    my_list = [ [] for _ in range(n) ]
    for _ in range(3):
        my_arr = my_rotate(my_arr)
        for i in range(len(my_arr)):
            my_list[i].append(''.join(map(str, my_arr[i])))

    print('#{}'.format(tc+1))
    for i in range(n):
        print(*my_list[i])

