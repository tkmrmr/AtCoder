N, K = map(int, input().split())
s = input()

count = 0
use_teeth = "O" * K

while 1:
    usable_teeth_first_index = s.find(use_teeth)
    if usable_teeth_first_index == -1:
        break
    else:
        count += 1
        s_list = list(s)
        s_list[usable_teeth_first_index : usable_teeth_first_index + K] = "X" * K
        s = "".join(s_list)

print(count)
