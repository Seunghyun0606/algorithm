# BJ. 14888 연산자 끼워넣기
# + - x / 순서


def operating(depth):

    if depth == n-1:
        num = nums[0]
        for i in range(n-1):
            if using[i] == 0:
                num += nums[i+1]
            elif using[i] == 1:
                num -= nums[i+1]
            elif using[i] == 2:
                num *= nums[i+1]
            else:
                if num < 0:
                    num = -(-num // nums[i+1])
                else:
                    num = num // nums[i+1]

        global num_max, num_min
        if num > num_max:
            num_max = num
        if num_min > num:
            num_min = num
    else:
        for i in range(4):
            if operator[i]:
                operator[i] -= 1
                using[depth] = i
                operating(depth+1)
                operator[i] += 1


n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))

using = [0] * (n-1)

num_max = -10 ** 9
num_min = 10 ** 9

operating(0)

print(num_max, num_min, sep='\n')

