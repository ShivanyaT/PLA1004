import sys
def solve():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = data[i]
        length = len(n)
        ans = []
        
        for idx, digit in enumerate(reversed(n)):
            if digit != '0':
                ans.append(int(digit) * (10 ** idx))
              
        out.append(str(len(ans)))
        out.append(" ".join(map(str, ans)))
        
    print("\n".join(out))
if __name__ == '__main__':
    solve()
