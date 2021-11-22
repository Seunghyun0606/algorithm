
word = input()

result = ''
result += word[0]
for w in range(1, len(word)):
    if word[w] == '-':
        result += word[w+1]
print(result)

# 똑똑한 풀이법
# A = list(input().split("-"))

# for i in range(len(A)):
#     print(A[i][0],end = "")