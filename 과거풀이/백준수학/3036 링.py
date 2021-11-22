from fractions import Fraction as F

n = int(input())

rings = list(map(int, input().split()))

ring = rings[0]

for i in range(1, n):
    print(F(ring, rings[i]) if not int(F(ring/rings[i])) == ring/rings[i] else str(F(ring, rings[i])) + '/1' )


# 다른 사람풀이 gcd이용
# def gcd(a, b):
#     mod = a%b
#     while mod > 0:
#         a = b
#         b = mod
#         mod = a%b
#     return b
# n=int(input())
# a=list(map(int,input().split()))
# for i in range(1,len(a)):
#     print("%d/%d"%(a[0]/gcd(a[0],a[i]),a[i]/gcd(a[0],a[i])))

# 다른사람 풀이 2
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def main():
#     input()
#     rings = map(int, input().split())
#     x = next(rings)
#     for ring in rings:
#         g = gcd(x, ring)
#         print(f"{x//g}/{ring//g}")

# main()