import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    count = 0
    idx = 1
    for _ in range(n):
        p = int(data[idx])
        q = int(data[idx+1])
        idx += 2
        
        if q - p >= 2:
            count += 1
            
    print(count)
if __name__ == '__main__':
    solve()
