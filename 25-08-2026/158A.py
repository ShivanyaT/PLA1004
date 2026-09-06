n, k = map(int, input().split())
scores = list(map(int, input().split()))

target_score = scores[k - 1]
advancers = 0

for score in scores:
    if score >= target_score and score > 0:
        advancers += 1

print(advancers)
