import sys

def main():
    year = int(sys.stdin.read().strip())
    while True:
        year += 1
        if len(set(str(year))) == 4:
            print(year)
            break
if __name__ == '__main__':
    main()
