N = int(input())

arr = []

arr.append(1)
arr.append(N)

while (True):
    if arr[-1] + arr[-2] > 100:
        arr.append(arr[-1] + arr[-2])
        break
    else:
        arr.append(arr[-1] + arr[-2])

print(*arr, end='')