import sys

def main():
    s = sys.stdin.read().splitlines()[0].lower()
    vowels = {'a', 'o', 'y', 'e', 'u', 'i'}
    res = ['.' + ch for ch in s if ch not in vowels]
    print(''.join(res))

if __name__ == '__main__':
    main()
