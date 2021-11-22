# 짝수면 두개

def solution(s):
    answer = ''

    if len(s) % 2:
        answer = s[len(s)//2]
    else:
        answer = s[len(s)//2-1:len(s)//2+1]
    return answer

# 짧게 구현 가능하다. 어차피 슬라이싱 쓸거면 아래와 같이 가능하다. 홀수면 어차피 하나 빼면 짝수가되서 딱 가운데 수 1개만 뽑아지고,
# 짝수면 홀수가되면서 반내림 하니깐 2개를 뽑을 수 있게 되는 것. 똑똑하다.
# def string_middle(str):
# return str[(len(str)-1)//2:len(str)//2+1]