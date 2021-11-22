
n = int(input())

used_key = [0]*26

def capital_check(words):
    for idx, word in enumerate(words):
        if ord(word[0]) > 96:
            if not used_key[ord(word[0]) - 97]:
                used_key[ord(word[0]) - 97] = 1
                return idx
        else:
            if not used_key[ord(word[0]) - 65]:
                used_key[ord(word[0])- 65] = 1
                return idx
    return -1

def word_check(words):
    for idx, word in enumerate(words):
        for i in range(1, len(word)):
            if ord(word[i]) > 96:
                if not used_key[ord(word[i]) - 97]:
                    used_key[ord(word[i]) - 97] = 1
                    words[idx] = word[:i] + '[' + word[i:i+1] + ']' + word[i+1:]
                    print(*words)
                    return True
            else:
                if not used_key[ord(word[i]) - 65]:
                    used_key[ord(word[i]) - 65] = 1
                    words[idx] = word[:i] + '[' + word[i:i+1] + ']' + word[i+1:]
                    print(*words)
                    return True

for _ in range(n):
    words = list(input().split())

    capital_idx = capital_check(words)
    if capital_idx > -1:
        words[capital_idx] = '[' + words[capital_idx][:1] + ']' + words[capital_idx][1:]
        print(*words)
        continue

    if word_check(words):
        continue
    
    print(*words)

    


    
    
