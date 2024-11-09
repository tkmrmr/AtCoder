from itertools import product

N = int(input())
q, r = [], []
for _ in range(N):
    x, y = map(int, input().split())
    q.append(x)
    r.append(y)

Q = int(input())
t, d = [], []
for _ in range(Q):
    x, y = map(int, input().split())
    t.append(x)
    d.append(y)

max_day = max(d) + max(q)

pools = product(range(Q), range(1, max_day + 1))

for i, j in pools:
    if j >= d[i] and j < d[i] + q[t[i] - 1] and j % q[t[i] - 1] == r[t[i] - 1]:
        print(j)
