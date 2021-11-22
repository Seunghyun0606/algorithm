T = int(input())

for _ in range(T):
    number_list = list(map(int, input().split()))
    numbers = 0
    for i in range(1, number_list[0]+1):
        numbers += number_list[i]
    check = 0
    for i in range(1, number_list[0]+1):
        if numbers/number_list[0] < number_list[i]:
            check += 1
    print('{:.3f}%'.format(round(check*100/number_list[0], 3)))