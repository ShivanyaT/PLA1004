import sys
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        if n == 1:
            results.append("1")
        elif n == 2:
            results.append("2 4")
        else:
            ans = []
            current_val = 2
            for _ in range(n):
                ans.append(str(current_val))
                current_val *= 2
            results.append(" ".join(ans))
            
    print("\n".join(results))

if __name__ == '__main__':
    solve()
