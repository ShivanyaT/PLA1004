count = 0
prev = ""
for _ in range(int(input())):
    curr = input()
    if curr != prev:
        count += 1
    prev = curr
print(count)
