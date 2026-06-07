N = int(input())
arr = list(input().split())

temp = ''.join(arr)
result = ''

for w in temp:
    result += w
    if len(result) == 5:
        print(result)
        result = ''

print(result)