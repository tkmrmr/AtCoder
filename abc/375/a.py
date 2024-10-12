n = input()
s = input()

count = 0

for i, _ in enumerate(s):
    if i >= len(s) - 2:
        break
    if s[i] == "#" and s[i + 1] == "." and s[i + 2] == "#":
        count += 1

print(count)
