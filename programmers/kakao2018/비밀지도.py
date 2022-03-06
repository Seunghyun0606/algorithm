# 이진수 만들고, 이진수 or 조건

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]

arr2 = [27 ,56, 19, 14, 14, 10]

answer = []

for i in range(n):
    my_bin = bin( arr1[i] | arr2[i] )

    while len(my_bin) < 2 + n:
        my_bin = '0' + my_bin

    temp = ''
    for i in range(2, 2 + n):
        if my_bin[i] == '1':
            temp += '#'
        else:
            temp += ' '
    answer.append(temp)
print(answer)


answer = []



print(bin(22|14))