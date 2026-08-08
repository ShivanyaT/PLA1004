for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        print(abs(2 - i) + abs(2 - row.index(1)))
        break