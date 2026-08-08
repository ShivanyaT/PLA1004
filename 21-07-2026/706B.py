import bisect
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    n = int(data[0])
    prices = [int(x) for x in data[1:n+1]]
    prices.sort()
    
    q = int(data[n+1])
    queries = [int(x) for x in data[n+2:n+2+q]]
    
    results = []
    for m in queries:
        ans = bisect.bisect_right(prices, m)
        results.append(str(ans))
        
    print('\n'.join(results))

if __name__ == '__main__':
    main()
