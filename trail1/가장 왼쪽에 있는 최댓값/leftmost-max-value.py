n = int(input())
a = list(map(int, input().split()))
result = []
# Please write your code here.

while len(a) > 0:
    max_val = max(a)
    idx = a.index(max_val)
    a = a[:idx]

    result.append(idx+1)

    if idx == 0:
        break

print(*result)