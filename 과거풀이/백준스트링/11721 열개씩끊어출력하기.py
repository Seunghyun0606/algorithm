word = input()

num = len(word)

for i in range(num//10):
    print(word[i*10:(i+1)*10])
print(word[num//10*10:])

# 슬라이싱에서 범위넘어가면 어차피 마지막꺼까지만 나오니깐, 이런식으로해도된다.
# for i in range(num//10 + 1):
#     print(word[i*10:(i+1)*10])

# for의 성질을 이용함. 똑똑하네
# l=input()
# for i in range(0,len(l),10):
#     print(l[i:i+10])
