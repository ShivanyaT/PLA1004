for _ in range(int(input())):
    w = input()
    print(w if len(w) <= 10 else f"{w[0]}{len(w)-2}{w[-1]}")
