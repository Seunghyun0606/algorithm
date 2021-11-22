# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임


def kbb_win(x, y):
    a = players[x]
    b = players[y]
    if a == 1 and b == 3:
        return x
    elif b == 1 and a == 3:
        return y
    elif a == b:
        return x  # a가 낮은 숫자의 플레이어
    elif a < b:
        return y
    elif a > b:
        return x


def kbb(alist):  # alist는 참여명단(players 리스트)

    if len(alist) == 1:
        return alist[0]

    # elif len(alist) == 2:
    #     return kbb_win(alist[0], alist[1])  # 이건 안해도된다. 왜냐면 어차피 밑에서 다 분할정복 할거니깐.

    else:

        mid = (len(alist) - 1) // 2 + 1  # 홀수일때 왼쪽꺼가 더커야함 ex) 3일때 2 / 1로 분할해야한다. 따라서 슬라이싱을위해 +1 더해준다.
        game1 = alist[:mid]
        game2 = alist[mid:]

        return kbb_win(kbb(game1), kbb(game2))  # 0, 1, 2, 3 번 사람을 넣어서 kbb_win에서 어떤사람이 이겼는지 뽑아낼꺼다.


T = int(input())

for tc in range(T):
    n = int(input())

    players = list(map(int, input().split()))

    print('#{} {}'.format(tc+1, kbb(range(n))+1))  # 0, 1, 2, 3 인덱스 이니깐 마지막에 +1 해줘야 몇번사람인지 알수있따.