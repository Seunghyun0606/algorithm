# 다중 집합 개념
# 다중집합 A = {1, 1, 2, 2, 3}, 다중집합 B = {1, 2, 2, 4, 5}라고 하면, 교집합 A ∩ B = {1, 2, 2}, 합집합 A ∪ B = {1, 1, 2, 2, 3, 4, 5}
# 다중집합을 일반 set 연산으로도 구할 수 있다.

# 두 문자열이 들어온다. 2 ~ 1000
# 2글자씩 끊어서 다중집합 원소, 대 소문자 구분 없고, 알파벳만 사용
# 둘다 공집합일 경우 1. 문자열이 2이상이라 해도, 알파벳이 없을 수 있다.


import re

p = re.compile('^[A-Z]*$')

str1 = 'aa1+aa2'
str2 = 'AAAA12'

str1 = str1.upper()
str2 = str2.upper()

new_str1 = []
new_str2 = []

# dictionary로 구분할 수 도 있지만, 이번엔 정규표현식 연습겸 정규표현식 사용.
for i in range(len(str1) - 1):
    temp_str = p.match(str1[i] + str1[i+1])
    if temp_str:
        new_str1.append(temp_str.group())
for i in range(len(str2) - 1):
    temp_str = p.match(str2[i] + str2[i+1])
    if temp_str:
        new_str2.append(temp_str.group())

set1 = set(new_str1)
set2 = set(new_str2)

# 다중 집합의 교집합
gyo = set1 & set2

multi_gyo = []
for g in gyo:
    for _ in range( min(new_str1.count(g), new_str2.count(g))):
        multi_gyo.append(g)

# 다중 집합의 합집합
multi_hap = []
hap = set1 | set2
for h in hap:
    for _ in range(max(new_str1.count(h), new_str2.count(h))):
        multi_hap.append(h)

# result = len(multi_gyo) * 65536 // len(multi_hap)

print(multi_gyo)
print(multi_hap)

