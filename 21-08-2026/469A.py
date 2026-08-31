import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    p = int(input_data[1])
    x_levels = [int(i) for i in input_data[2 : 2 + p]]
    idx_y = 2 + p
    q = int(input_data[idx_y])
    y_levels = [int(i) for i in input_data[idx_y + 1 : idx_y + 1 + q]]
    combined_levels = set(x_levels) | set(y_levels)
    if len(combined_levels) == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")

if __name__ == '__main__':
    solve()
