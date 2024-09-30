import numpy as np

n, m = map(int, input().split(" "))
u, v, w = [], [], []

g = np.zeros((1, n))
g_w = np.zeros((1, n))

for _ in range(m):
    u_i, v_i, w_i = map(int, input().split(" "))
    u.append(u_i)
    v.append(v_i)
    w.append(w_i)
print(g)

# for i in range(m):
#     np.append(g[u[i]], v[i])
#     np.append(g_w[u[i]], w[i])

