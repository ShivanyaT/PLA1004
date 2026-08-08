import sys

def main():
    n, m, a = map(int, sys.stdin.readline().split())
    flagstones_n = (n + a - 1) // a
    flagstones_m = (m + a - 1) // a
    print(flagstones_n * flagstones_m)

if __name__ == '__main__':
    main()
