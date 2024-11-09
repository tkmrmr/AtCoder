def judge(n, m, x, a):
    if sum(a) < n:
        return -1

    for i in range(m - 1):
        if a[i] < x[i + 1] - x[i]:
            return -1

    if a[-1] < (n - 1) - x[-1]:
        return -1

    if not 0 in x:
        return -1

    masses = [0] * n
    zeroes = [i for i, _ in enumerate(masses)]

    for i, _ in enumerate(x):
        masses[x[i]] = a[i]
        zeroes.remove(x[i])

    count = 0

    while zeroes:
        zero_index = zeroes.pop(0)
        if masses[zero_index - 1] == 1:
            masses[zero_index] = 1
            masses[zero_index - 1] = 0
            zeroes.append(zero_index - 1)
            count += 1
        else:
            masses[zero_index] = 1
            masses[zero_index - 1] -= 1
            count += 1

    return count


N, M = map(int, input().split())
x = list(map(lambda x: int(x) - 1, input().split()))
a = list(map(int, input().split()))

print(judge(N, M, x, a))
