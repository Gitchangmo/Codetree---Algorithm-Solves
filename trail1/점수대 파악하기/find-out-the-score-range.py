nums = list(map(int, input().split()))

scores = [0] * 11

for num in nums:
    if num == 0:
        break
    count_score = num // 10
    if count_score > 0:
        scores[count_score] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {scores[i]}")   