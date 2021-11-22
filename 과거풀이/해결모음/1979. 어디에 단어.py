# 1979 어디에 단어가 있을까? D2

T = int(input())

for tc in range(T):

    n, k = map(int, input().split())  # n는 nxn 행렬, k는 단어길이
    array = [ list(map(int, input().split())) for _ in range(n) ]

    word_count = 0
    for x in range(len(array)):  # n 배열의 반복작업을 위함
        count_col = 0
        count_row = 0
        y = 0
        while y < len(array):  # n 배열의 반복작업을 위함
            if array[x][y] == 1:  # 열 검색
                count_col += 1
            if array[y][x] == 1:  # 행 검색
                count_row += 1

            if array[x][y] == 0 or y == len(array)-1:
                if count_col == k:  # 0을만나면 이전까지 카운트가 k개인지 확인하고 맞으면 +1 하고 초기화
                    word_count += 1
                    count_col = 0
                else:
                    count_col = 0
            if array[y][x] == 0 or y == len(array)-1:
                if count_row == k:
                    word_count += 1
                    count_row = 0
                else:
                    count_row = 0
            y += 1

    print('#{}'.format(tc+1), word_count)