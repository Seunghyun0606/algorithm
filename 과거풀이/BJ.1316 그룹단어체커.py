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

cnt = 0
for i in range(int(input())):
    word = input()
    # 찾는 순서대로 정렬
    # 찾는 순서대로 정렬하고나서 input으로 받았던 string 과 다르다면 Not counting
    # list(hello)=['h', 'e', 'l', 'l', 'o']
    print(sorted(word, key=word.find))
    cnt += list(word) == sorted(word, key=word.find)

print(cnt)
