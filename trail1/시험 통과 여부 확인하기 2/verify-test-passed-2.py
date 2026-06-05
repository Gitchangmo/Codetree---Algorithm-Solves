N = int(input())

count = 0

for i in range(N):
    scores = list(map(int, input().split()))
    Avg = sum(scores) / len(scores)
    if Avg >= 60:
        print("pass")
        count += 1
    else:
        print("fail")

print(count)