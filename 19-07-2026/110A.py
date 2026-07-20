s = input()
lucky_count = s.count('4') + s.count('7')
if lucky_count == 4 or lucky_count == 7:
    print("YES")
else:
    print("NO")
