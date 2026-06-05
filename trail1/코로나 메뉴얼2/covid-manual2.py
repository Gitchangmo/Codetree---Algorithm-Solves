arr = [0] * 4

for _ in range(3):
    symp, temp = input().split()
    temp = int(temp)
    if (symp == 'Y' and temp >= 37):
        arr[0] += 1
    elif (symp == 'N' and temp >= 37):
        arr[1] += 1
    elif (symp == 'Y' and temp < 37):
        arr[2] += 1
    else:
        arr[3] += 1

print(*arr, end='')

if arr[0] >= 2:
    print(' E')