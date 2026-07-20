import sys
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1 
    out = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        a = [int(x) for x in data[idx:idx+n]]
        idx += n
        
        b = [int(x) for x in data[idx:idx+m]]
        idx += m
        b.append(0)
        b.sort()
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + a[i]
        ans = 0
        for i in range(1, len(b)):
            ans += abs(pref[b[i]] - pref[b[i-1]])
        ans += pref[n] - pref[b[-1]]
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
