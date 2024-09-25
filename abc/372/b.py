m = int(input())
a = []
while(m > 0):
    for i in range(10, -1, -1):
        if m >= 3**i:
            a.append(str(i))
            m -= 3**i   
            break
print(len(a))
print(" ".join(a))
        