word = input()

alpha_list = [-1]*26

for w in range(len(word)):
    if alpha_list[ord(word[w])-97] < 0:
        alpha_list[ord(word[w])-97] = w

print(*alpha_list)
