
dial = input()
count = 0
for d in dial:
    if d in "ABC":
        count += 3
    elif d in "DEF":
        count += 4
    elif d in "GHI":
        count += 5
    elif d in "JKL":
        count += 6
    elif d in "MNO":
        count += 7
    elif d in "PQRS":
        count += 8
    elif d in "TUV":
        count += 9
    elif d in "WXYZ":
        count += 10

else:
    print(count)