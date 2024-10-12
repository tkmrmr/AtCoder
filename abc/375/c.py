import numpy as np
import copy

n = int(input())
grid = []

for _ in range(n):
    grid.append(list(input()))

grid_cp = copy.deepcopy(grid)

for i in range(int((n - 1) / 2)):
    for j in range(i, n - i - 1):
        grid[i][n - j - 1] = grid_cp[j][i]
        grid[j][n - i - 1] = grid_cp[i][j]
    print("--------------------")
    [print(line) for line in grid]
    grid_cp = copy.deepcopy(grid)

print("--------------------")
[print(line) for line in grid]
