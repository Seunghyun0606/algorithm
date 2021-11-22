# 4408. 자기 방으로 돌아가기
# 최소 1, 겹칠때마다 count + 1

T = int(input())

for tc in range(T):

    n = int(input())

    rooms = [ list(map(int, input().split())) for _ in range(n) ]

    check = [0] * 401

    for i in range(n):
        if rooms[i][0] > rooms[i][1]:
            if rooms[i][0] % 2:  # 앞이 홀
                if rooms[i][1] % 2:  # 뒤가 홀
                    for j in range(rooms[i][0], rooms[i][1]+1):
                        check[j] += 1
                else:  # 홀 짝
                    for j in range(rooms[i][0], rooms[i][1]):
                        check[j] += 1

            else:
                if rooms[i][1] % 2:  # 짝 홀
                    for j in range(rooms[i][0]-1, rooms[i][1]+1):
                        check[j] += 1
                else:  # 짝 짝
                    for j in range(rooms[i][0]-1, rooms[i][1]):
                        check[j] += 1
        else:
            if rooms[i][1] % 2:  # 앞이 홀
                if rooms[i][0] % 2:  # 홀 홀
                    for j in range(rooms[i][1], rooms[i][0]-1, -1):
                        check[j] += 1
                else: # 홀 짝
                    for j in range(rooms[i][1], rooms[i][0]-2, -1):
                        check[j] += 1
            else:
                if rooms[i][0] % 2:  # 짝 홀
                    for j in range(rooms[i][1]-1, rooms[i][0] - 1, -1):
                        check[j] += 1
                else:  # 짝 짝
                    for j in range(rooms[i][1]-1, rooms[i][0] - 2, -1):
                        check[j] += 1

    print('#{}'.format(tc+1), max(check))



