import collections

a = list(map(int, input().split()))

c = collections.Counter(a)

count = 0

for key, value in c.items():
    if value == 1:
        pass
    elif value == 2:
        count += 1
    elif value == 3:
        count += 1
    elif value == 4:
        count += 2

print(count)
