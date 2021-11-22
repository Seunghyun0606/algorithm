words = input()

result = words.count(' ') + 1
if words[0] == ' ':
    result -= 1
if words[-1] == ' ':
    result -= 1
print(result)

# print(len(input().split())) 이렇게해도된다. 다만 속도와 메모리가 count보다 느리고 많이먹는다.