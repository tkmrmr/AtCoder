import math


def get_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance


ps = [(0, 0)]
n = int(input())

for _ in range(n):
    p = tuple(map(int, input().split(" ")))
    ps.append(p)

cost = 0

for i in range(n):
    cost += get_distance(ps[i], ps[i + 1])

cost += get_distance(ps[n], ps[0])

print(cost)
