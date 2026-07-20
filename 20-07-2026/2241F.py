import sys
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    out = []
    
    for i in range(1, t + 1):
        n = int(data[i * 2 - 1])
        s = data[i * 2]
        
        ones = 0
        total_inv = 0
        for char in s:
            if char == '1':
                ones += 1
            else:
                total_inv += ones
        if total_inv % 2 == 1:
            out.append("ALICE")
            continue
        found_win = False
        current_ones = 0
        for idx in range(n):
            if s[idx] == '1':
                current_ones += 1
            else:
                left_inv = current_ones
                right_inv = total_inv - current_ones
                # Valid move condition
                if (left_inv % 2 == 1) or (right_inv % 2 == 1):
                    found_win = True
                    break
                    
        if found_win:
            out.append("ALICE")
        else:
            out.append("BOB")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
