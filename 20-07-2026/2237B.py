import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    ptr = 0
    t = int(data[ptr])
    ptr += 1
    out = []
    for _ in range(t):
        n = int(data[ptr])
        ptr += 1
        a = [int(x) for x in data[ptr:ptr+n]]
        ptr += n
        b = [int(x) for x in data[ptr:ptr+n]]
        ptr += n
        
        a_sorted = sorted([(a[i], i) for i in range(n)])
        
        visited = [False] * n
        swaps = 0
        a_ptr = 0
        
        for bi in b:
            while a_ptr < n and a_sorted[a_ptr][0] <= bi:
                a_ptr += 1
            
            found_idx = -1
            for j in range(a_ptr):
                if not visited[j]:
                    found_idx = j
                    break
            if found_idx == -1:
                swaps = -1
                break
             visited[found_idx] = True
            
            unvisited_before = sum(1 for k in range(found_idx) if not visited[k])
            swaps += unvisited_before
            
        out.append(str(swaps))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
