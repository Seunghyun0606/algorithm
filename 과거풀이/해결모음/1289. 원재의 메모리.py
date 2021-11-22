# 1289. 원재의 메모리 구하기

# 원래 값의 맨 첫 값을 검색해서 1이들어가면 그때부터 시작, 연속하는 숫자가 다르면 count를 세주면된다
# 예를들어 원래값이 10101 이었으면 00000에서 시작해서 11111 10000 10111 10100 10101 총 5번이 된다.

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):

    memory = str(input())
    count = 0

    for i in range(len(memory)):
        if memory[i] == '1':
            count += 1
            for j in range(i+1, len(memory)):
                if memory[j-1] != memory[j]:
                    count += 1
            break
    print('#{}'.format(tc+1), count)
