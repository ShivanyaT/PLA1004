n = int(input())

lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

is_almost_lucky = False
for lucky in lucky_numbers:
    if n % lucky == 0:
        is_almost_lucky = True
        break

if is_almost_lucky:
    print("YES")
else:
    print("NO")
