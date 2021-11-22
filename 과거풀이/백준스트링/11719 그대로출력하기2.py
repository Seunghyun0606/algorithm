while True:
    try:
        print(input())
    except EOFError:
        break

# 다른방법
# import sys
# print(sys.stdin.read())