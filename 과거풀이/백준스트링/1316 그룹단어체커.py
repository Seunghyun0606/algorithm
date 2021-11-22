
n = int(input())
cnt = 0
for _ in range(n):
    check = ''
    check_word = ''
    for word in input():
        if check != word:
            if word in check_word:
                break
            check = word
            check_word += word
    else:
        cnt += 1
print(cnt)

# 과거풀이, defaultdict사용. 오히려 이게 불편하고 느림
# n = int(input())
# from collections import defaultdict
# count = 0
# for i in range(n):
#     check = defaultdict(int)
#     word = input()
#     if len(word) == 1:
#         count += 1
#         continue
#     check[word[0]] += 1
#     for idx in range(1, len(word)):
        
#         if word[idx] != word[idx-1]:
            
#             if check[word[idx]]:
#                 break
#             else:
#                 check[word[idx]] += 1
#     else:
#         count += 1

# print(count)

# 빠른풀이?
# result = 0
# for i in range(int(input())):
#     word = input()
#     # print(sorted(word, key=word.find))
#     if list(word) == sorted(word, key=word.find):
#         result += 1
# print(result)