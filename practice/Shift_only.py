n = input()
a = list(map(int, input().split(" ")))
count = 0
while(1):
    a_mod = list(map(lambda x: x%2 ,a))
    if 1 in a_mod:
        break
    a = list(map(lambda x: x/2 ,a))
    count += 1
print(count)


