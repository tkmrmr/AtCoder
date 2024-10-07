s = input()
t = input()

max_len = max(len(s), len(t))

if s == t:
    print(0)
    exit()

for i in range(max_len):
    try:
        if s[i] == t[i]:
            continue
        else:
            print(i + 1)
            break
    except:
        print(i + 1)
        break
