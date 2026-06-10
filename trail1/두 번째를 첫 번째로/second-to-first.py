S = input()

arr = list(S)
first = arr[0]
second = arr[1]

for idx, w in enumerate(arr):
    if w == second:
        arr[idx] = first

print(''.join(arr))