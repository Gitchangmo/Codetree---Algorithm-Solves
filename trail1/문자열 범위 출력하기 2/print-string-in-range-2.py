arr = input()
idx = int(input())

if len(arr) >= idx:
    print(arr[-1:-idx-1:-1])
else:
    print(arr[::-1])