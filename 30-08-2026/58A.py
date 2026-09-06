s = input()
target = "hello"
target_index = 0

for char in s:
    if char == target[target_index]:
        target_index += 1
        if target_index == 5:
            break

if target_index == 5:
    print("YES")
else:
    print("NO")
