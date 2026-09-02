n = int(input())
bills = [100, 20, 10, 5, 1]
ans = 0
for bill in bills:
    ans += n // bill
    n %= bill

print(ans)
