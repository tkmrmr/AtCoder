n, q = map(int, input().split(" "))
s = input()
count = s.count("ABC")
for i in range(q):
    x, c = input().split(" ")
    count_around_x = s[int(x)-1-2:int(x)-1+3].count("ABC")
    s_list = list(s)
    s_list[int(x)-1] = c
    s = "".join(s_list)
    count_around_x_new = s[int(x)-1-2:int(x)-1+3].count("ABC")
    count = count - count_around_x + count_around_x_new
    print(count)