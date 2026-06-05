A, B = map(int, input().split())

arr = [0] * 10

while A > 1:
    Quot = A // B
    Remind = A % B
    arr[Remind] += 1
    A = Quot

result = 0

for num in arr:
    result += num ** 2

print(result)