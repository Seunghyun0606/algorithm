T = int(input())

for _ in range(T):
    h = int(input())
    w = int(input())
    apart = [ [ i+1 for i in range(14) ] ]

    for k in range(14):  # 0층은 있으니, 14층구해야함.
        temp = []
        for j in range(1, 15):  # 여기까지가 한층을 구하는 것,
            temp_value = 0
            for i in range(j):
                temp_value += apart[k][i]
            else:
                temp.append(temp_value)
        else:
            apart.append(temp)
    print(apart[h][w-1])