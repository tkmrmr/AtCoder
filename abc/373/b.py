s = input()
move_distance = 0
position = str.find(s, "A")
char = "A"
for _ in range(25):
    next_char = chr(ord(char) + 1)
    next_position = str.find(s, next_char)
    move_distance += abs(next_position - position)
    char = next_char
    position = next_position
print(move_distance)